import i2cUtils as ic

import numpy as np
import matplotlib.pyplot as plt
import time
import i2cUtils as ic
import RPi.GPIO as GPIO
import math as calc

import spiUtils as su



# Use GPIO numbering
GPIO.setmode(GPIO.BCM)

# Assign a variable for the pin numer
switchPin = 24

# Configures the GPIO pin to accept inputs
# GPIO.PUD_UP:   pull-up   resistor = high V when the switch is open
# GPIO.PUD_DOWN: pull-down resistor = high V when the switch is closed
GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print(GPIO.input(switchPin))

# Create a class for your accelerometer with the following methods (feel free to add more):
# getAcceleration()
# Returns the 3 accelerometer arrays given by the readACC() function
# getAccelerationX()
# Returns the acceleration only in the x-direction.
# getAccelerationY()
# Returns the acceleration only in the y-direction.
# getAccelerationZ()
# Returns the acceleration only in the z-direction.
# getMagnitude()
# Returns the magnitude of acceleration measured by the sensor.
# Your code only needs to collect one set of data after the switch flips. Once




class Accelerometer:
    def __init__(self,xVal = 0,yVal = 0,zVal = 0,mag = 0): 
        self.X = xVal
        self.Y = yVal
        self.Z = zVal
        self.Mag = mag

    def readAcceleration(self):
        self.X,self.Y,self.Z = ic.readACC()

    def getAcceleration(self):
         self.readAcceleration()
         return self.X, self.Y, self.Z
        
    
    def getAccelerationX(self):
        #self.readAcceleration()
        return self.X


    def getAccelerationY(self):
        #self.readAcceleration()
        return self.Y

    def getAccelerationZ(self):
        #self.readAcceleration()
        return self.Z

    def getMagnitude(self):
        return calc.sqrt(pow(self.X,2)+pow(self.Y,2)+pow(self.Z,2))
        
#TODO: Find a better way of allocation memory for the numpy arrays - clp
nDATA = 2000

xACC = np.zeros(nDATA,dtype='float')
yACC = np.zeros(nDATA,dtype='float')
zACC = np.zeros(nDATA,dtype='float')
mACC = np.zeros(nDATA,dtype='float')
tACC = np.zeros(nDATA,dtype='float')

toVolt = 3.3/1023
dPIEZO = np.zeros(nDATA,dtype='float')
acclerometer = Accelerometer()

while True:
    state = GPIO.input(switchPin) # TILT switch
    if state: # If tilt switch active get data
        # Accelerometer Data
        ax,ay,az = ic.readACC()
        print(ax,ay,az)
        ti = time.time()
        i = 0
        while (time.time() - ti) <= 15:
           
            dPIEZO[i] = toVolt * su.readADC(channel=0) # PIEZO element
            tACC[i] = time.time() - ti
            print(acclerometer.getAcceleration())
            xACC[i] = acclerometer.getAccelerationX()
            yACC[i] = acclerometer.getAccelerationY()
            zACC[i] = acclerometer.getAccelerationZ()
            mACC[i] = acclerometer.getMagnitude()
            i +=1

            

np.savez('flatEarth.npz', tACC,xACC,yACC,zACC,mACC,dPIEZO) 
plt.plot(tACC,xACC,'r')
plt.show()
plt.plot(tACC,yACC,'g')
plt.show()
plt.plot(tACC,zACC,'b')
plt.show()
plt.plot(dPIEZO,'k')
plt.show()