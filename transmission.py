import serial
import time 

ser=serial.Serial("/dev/ttyACM0",baudrate=9600,bytesize=8,parity='N',stopbits=1)


while 1: 

    #incoming=ser.readline()

   # if incoming == 'A' :
    ser.write('/n')
    #if incoming == 'B':
     #   ser.write('A')

    print("sending 'A' to arduino")
    time.sleep(4)
    print("Listening to channel")
    inputdata =  ser.readline()
    
    print(inputdata)
#    time.sleep(10)
 #   ser.write("B\n")
  #  print("sending 'B' to Arduino")
   # time.sleep(10)
    #print("Listening to Channel")
   # inputdata = ser.readline() 

ser.close()
