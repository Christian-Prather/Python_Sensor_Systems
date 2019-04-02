import spidev

# Don't modify this function!
# If you want to use a different function, include it with your submission!
def readADC(channel=0):
    spi = spidev.SpiDev()       # Create a new spidev object
    spi.open(0,0)               # Open communication on bus 0 and CE0
    spi.max_speed_hz = int(1e5) # Set clock speed to 100 kHz
  
    if(channel==0): config = [0b01101000, 0] # Measure from channel 0
    else:           config = [0b01111000, 0] # Measure from channel 1

    myBytes = spi.xfer2(config)             # Send and get array of 2 bytes from ADC
    myData = (myBytes[0] << 8) | myBytes[1] # Convert returned bytes to integer value
    
    spi.close()   # Stop communication with ADC
    
    return myData # Return measurement (integer from 0 to 1023)