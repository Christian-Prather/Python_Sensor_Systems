import i2cUtils as ic

import numpy as np
import matplotlib.pyplot as plt
import time
import i2cUtils as ic
import RPi.GPIO as GPIO

import spiUtils as su


for i in range(nDATA):

# Use GPIO numbering
GPIO.setmode(GPIO.BCM)

# Assign a variable for the pin numer
switchPin = 24

# Configures the GPIO pin to accept inputs
# GPIO.PUD_UP:   pull-up   resistor = high V when the switch is open
# GPIO.PUD_DOWN: pull-down resistor = high V when the switch is closed
GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print(GPIO.input(switchPin))

class Accelerometer:
    def 

nDATA = 2000
xACC = np.zeros(nDATA,dtype='float')
yACC = np.zeros(nDATA,dtype='float')
zACC = np.zeros(nDATA,dtype='float')
tACC = np.zeros(nDATA,dtype='float')

toVolt = 3.3/1023
dPIEZO = np.zeros(nDATA,dtype='float')

while True:
    state = GPIO.input(switchPin) # TILT switch
    if state: # If tilt switch active get data
        # Accelerometer Data
        ax,ay,az = ic.readACC()
        print(ax,ay,az)
        ti = time.time()
        for i in range(nDATA):
            xACC[i], yACC[i], zACC[i] = ic.readACC()
            dPIEZO[i] = toVolt * su.readADC(channel=0) # PIEZO element
            tACC[i] = time.time() - ti
            if tACC[i] > 15:
                break
        ####################



# TODO Plot these as subplots on own plots
np.savez('flatEarth.npz', tACC,xACC,yACC,zACC,dPIEZO) 
plt.plot(tACC,xACC,'r')
plt.plot(tACC,yACC,'g')
plt.plot(tACC,zACC,'b')
plt.plot(dPIEZO,'k')

plt.show()