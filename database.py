#/!usr/bin/python
import MySQLdb
import sys

#inputvalue = int(input("Enter a value  "))
#print(inputvalue)

def ObtainReadings():
#connect to the SensorInformation database.
    database = MySQLdb.connect(host="localhost",user="root",passwd="1",db="SensorInformation")

#Create a pointer in that database

    cursor = database.cursor()
    list = []
#information = cursor.execute("SELECT Readings from pHOutput ORDER BY time DESC limit 8")
    cursor.execute("SELECT Readings from pHOutput")
    result = cursor.fetchall()
    database.commit()
    cursor.close()
    database.close()

    for t in result: 
        list.append(float(t[0]))
        
        
    return(list)

my_list = ObtainReadings()
print(my_list)

