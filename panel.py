#!/usr/bin/python
# -*- coding: utf-8 -*-

# size.py

import wx
import numpy as np
import pylab as py
import MySQLdb
import sys
import time 



class GUI(wx.Frame): #creates the frame object
  #constructor for the Example class. 
    def __init__(self, parent, title):
        super(GUI, self).__init__(parent, title=title, 
            size=(1000, 1000))
       
        self.InitUI()            
        self.Show()
   # Initialization function to get everything setup. 
    def InitUI(self):
    
    #define menubar
        #menubar = wx.MenuBar()
        #settingMenu = wx.Menu() 
        #fileMenu = wx.Menu()    
        #menubar.Append(fileMenu,'File')
        #menubar.Append(settingMenu,'Settings')
        #self.SetMenuBar(menubar)
        
        panel = wx.Panel(self,-1)
        #Set the background color of the panel. 
        panel.SetBackgroundColour('#A6A88F')
        #Add the grid structure to the panel.
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((-1,100))
        
        #Insert Logo
        img = wx.Image('/home/pi/python-scripts/icon1.png',wx.BITMAP_TYPE_ANY)
        img.Rescale(500,300)
        logo = wx.StaticBitmap(panel,wx.ID_ANY,wx.BitmapFromImage(img))
        vbox.Add(logo,flag=wx.ALIGN_LEFT)

        #Organize button layout.
        buttons = wx.BoxSizer(wx.VERTICAL)
        pHbutton = wx.Button(panel,wx.ID_ANY,'Display pH Readings')
        Tempbutton = wx.Button(panel,wx.ID_ANY,'Display Temperature Readings')
        Condbutton = wx.Button(panel,wx.ID_ANY,'Display Conductivity Readings')
        
        
        
        
        #Add buttons to button layout
        sensor_info_label = wx.StaticBox(panel,label = 'Sensor Readings')
        buttons.Add(sensor_info_label,flag=wx.LEFT)
        buttons.Add(pHbutton,flag=wx.LEFT)
        buttons.Add(Tempbutton,flag=wx.LEFT)
        buttons.Add(Condbutton,flag=wx.LEFT)

       
        

        #Organize Plant Species Option 
        species = ['Lettuce','Spicy Lettuce','Mixture','Flower']
        plntcb = wx.ComboBox(panel,choices=species,style=wx.CB_READONLY)
        plantspecies = wx.BoxSizer(wx.VERTICAL)
       
        #ADD LABEL FOR DROP DOWN BOX
        plant_label = wx.StaticBox(panel, label = 'Plant Species')
        plantspecies.Add(plant_label,flag=wx.LEFT)
        plantspecies.Add(plntcb,flag=wx.LEFT)
        
        #Add response to drop down box
        
        st = wx.StaticText(panel,label='')
        vbox.Add(buttons,flag=wx.ALIGN_RIGHT|wx.RIGHT,border = 100)
        vbox.Add((-1,90))
        vbox.Add(plantspecies,flag=wx.ALIGN_RIGHT|wx.RIGHT,border = 110)
        vbox.Add((-1,20))
        #vbox.Add(st,flag=wx.ALIGN_RIGHT|wx.RIGHT, border = 110)
        panel.SetSizer(vbox)

       #Bind  Events. 
        self.Bind(wx.EVT_BUTTON, self.pHbuttonpress, id=pHbutton.GetId())
        self.Bind(wx.EVT_BUTTON, self.Tempbuttonpress,id=Tempbutton.GetId())
        self.Bind(wx.EVT_BUTTON, self.CondbuttonPress, id = Condbutton.GetId())
        plntcb.Bind(wx.EVT_COMBOBOX, self.comboEvent)

    def comboEvent(self,e):
        alert = wx.MessageDialog(None,'Target Parameters: pH = 6.2 ,  Temperature = 25 celsius,    Conductivity= 600ppm','Note: Adjustments Made',wx.ICON_EXCLAMATION | wx.OK)
        alert.ShowModal()

    def pHbuttonpress(self, e):
        count = 2
        MaxProgress = 62
        status = wx.ProgressDialog("Obtaining Data","Status",MaxProgress,style=wx.PD_ELAPSED_TIME | wx.PD_AUTO_HIDE) 
        status.Update(count)
        count = count + 10
        status.Update(count)
        wx.Sleep(1)
        count = count + 10
        status.Update(count)
        wx.Sleep(1)
        py.xlabel('most recent samples')
        count = count + 10
        status.Update(count)
        wx.Sleep(1)
        py.ylabel(' Readings ')
        count = count + 10
        status.Update(count)
        wx.Sleep(1)
        py.title('PH Readings')
        count = count + 10
        status.Update(count)
        
        #Create a array of integers based on sensor readings. 
        Y = []
        Y = Obtain_pH_Readings()
        py.plot(Y,'r')
        count = count + 10 
        status.Update(count)
        status.Destroy()
        
        py.show()
        
        

    def Tempbuttonpress(self,e):
        count = 2
        MaxProgress = 42
        status = wx.ProgressDialog("Obtaining Data","Status",MaxProgress,style=wx.PD_ELAPSED_TIME | wx.PD_AUTO_HIDE)
        status.Update(count)
        count = count + 5
        status.Update(count)
        wx.Sleep(1)
        #Create a array of integers based on sensor readings. 
        Y=[]
        Y = Obtain_temp_Readings()
        count = count + 20
        status.Update(count)
        py.xlabel('sample number')
        py.ylabel('Readings')
        count = count + 10
        status.Update(count)
        py.title('Temperature Readings')
        py.plot(Y,'r')
        count = count + 5
        status.Update(count)
        status.Destroy()
        py.show()
   
    def CondbuttonPress(self,e):
        count = 2
        MaxProgress = 42
        status = wx.ProgressDialog("Obtaining Data","Status",MaxProgress,style=wx.PD_ELAPSED_TIME | wx.PD_AUTO_HIDE)
        #Create a array of integers based on sensor readings.
        Y = []
        Y = Obtain_Conduct_Readings()
        count = count + 20
        status.Update(count)
        py.xlabel('sample number')
        count = count + 5
        status.Update(count)
        py.ylabel('Readings')
        py.title('Conductivity Readings')
        count = count + 10 
        status.Update(count)
        py.plot(Y,'r')
        count = count + 5
        status.Update(count)
        status.Destroy()
        py.show()


def Obtain_pH_Readings():
#connect to the SensorInformation database.
    database = MySQLdb.connect(host="localhost",user="root",passwd="1",db="SensorInformation")

#Create a pointer in that database

    cursor = database.cursor()
    list = []
    cursor.execute("SELECT Readings from pHOutput ORDER BY time DESC limit 8")
    result = cursor.fetchall()
    database.commit()
    cursor.close()
    database.close()

    for t in result: 
        list.append(float(t[0]))
        
    return(list)

def Obtain_Conduct_Readings():
#connect to the SensorInformation database.
    database = MySQLdb.connect(host="localhost",user="root",passwd="1",db="SensorInformation")

#Create a pointer in that database

    cursor = database.cursor()
    list = []
#information = cursor.execute("SELECT Readings from pHOutput ORDER BY time DESC limit 8")
    cursor.execute("SELECT Readings from ConductivityOutput ORDER BY time DESC limit 8")
    result = cursor.fetchall()
    database.commit()
    cursor.close()
    database.close()

    for t in result: 
        list.append(float(t[0]))
        
    return(list)

def Obtain_temp_Readings():
#connect to the SensorInformation database.
    database = MySQLdb.connect(host="localhost",user="root",passwd="1",db="SensorInformation")

#Create a pointer in that database

    cursor = database.cursor()
    list = []
#information = cursor.execute("SELECT Readings from pHOutput ORDER BY time DESC limit 8")
    cursor.execute("SELECT Readings from tempOutput ORDER BY time DESC limit 8")
    result = cursor.fetchall()
    database.commit()
    cursor.close()
    database.close()

    for t in result: 
        list.append(float(t[0]))
        
    return(list)




        




if __name__ == '__main__':
  
    app = wx.App()
    GUI(None, title='NCIIA_CONS_BETA_GUI')
    app.MainLoop()
