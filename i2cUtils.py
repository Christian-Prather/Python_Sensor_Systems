import smbus

# Don't modify this function!
# If you want to use a different function, include it with your submission!
def readACC(i2cport=1):    
    
    # create a new smbus object
    bus = smbus.SMBus(i2cport)  

    # set to active mode to read from registers
    bus.write_byte_data(0x1D, 0x2A, 1)

    # read data from 6 registers
    data = bus.read_i2c_block_data(0x1D, 0x01, 6)

    # convert data from registers to single numbers
    xRaw = (data[0] << 4) + (data[1] >> 4)
    yRaw = (data[2] << 4) + (data[3] >> 4)
    zRaw = (data[4] << 4) + (data[5] >> 4)

    # fix for 2's complement numbers
    if xRaw >> 11 == 1:
        xRaw -= 2**12
    if yRaw >> 11 == 1:
        yRaw -= 2**12
    if zRaw >> 11 == 1:
        zRaw -= 2**12
    
    # convert to acceleration
    toAcc = 9.81 / 1024 
    
    xRaw *= toAcc
    yRaw *= toAcc
    zRaw *= toAcc
    
    # return data tuple
    return xRaw,yRaw,zRaw