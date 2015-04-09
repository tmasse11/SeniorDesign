import serial
import time

try:
    print "Trying..."
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    
except:
    print "Failed to connect on device"

    time.sleep(1)
while 1:
    
        
    print arduino.readline()
    time.sleep(1)
    
    



#try:
  # for i in range(3):
      # time.sleep(1)
     #  var = raw_input("Light on Y/N: ")
    #   print i
   #    arduino.write(var)
  #     print arduino.readline()
#except:
 #   print "Failed to send!"
  
