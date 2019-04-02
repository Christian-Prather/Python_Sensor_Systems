# Import libraries for use plotting, gpio, arrays, time
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
import time


# Pin declaration
buzzerPin = 25
switchPin = 27
ledPin = 21

# Declaration of global lists for plotting
duration= []
pitch=[]
order=[] 

# Bool variable for graphing and singing or just data logging (True = graphing, False = logging) 
singing = True


# Sets pins as output or input and set internal pull downs
def setupPins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzerPin, GPIO.OUT)
    GPIO.setup(switchPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(ledPin, GPIO.OUT)

# Reads a passed file and either returns the data as a 2D array/list of parses the data and logs info about it
def doFileIO(fileName, read = True):
    # Seperate the data by spaces
    data = np.loadtxt(fileName, delimiter= ' ')
    
    # Parse through the file for the max pitch value
    maxPitch = 0
    for note in data:
        if note[0] > maxPitch:
            maxPitch = note[0]

    # If in singing mode return the 2D list
    if read:
        return data
    # Else log the max pitch to logger.txt
    else:
        
        timeStamp = time.time()
        logEntry = maxPitch
        print("Max Pitch is", logEntry, "and has been logged to logger.txt")
        dataLogged = (str(logEntry), str(timeStamp)) 
        file = open ("logger.txt", 'a')
        file.write(str(dataLogged))
        file.close()
        
# Function for buzzing note, takes in frequency and durration from parsed file       
def buzz(pitch, duration):

    # Calculate note run time and cycles
    period = 1.0/pitch
    delay = period / 2
    cycles = int(duration * pitch)
    
    # Loop until note is played through
    for i in range(cycles):
        # Create a sqaure wave by outputting high, waiting, outputting low, waiting, then repeating
        # Turn on LED with each pulse
        GPIO.output(buzzerPin, True)
        GPIO.output(ledPin, True)
        time.sleep(delay)
        GPIO.output(buzzerPin, False)
        GPIO.output(ledPin, False)
        time.sleep(delay)
    time.sleep(duration * 0.3)

# Function for plotting frequncy of each note 
def plotData():
    plt.title("Pitch in Order")

    # Pass the global order and pitch arrays (order is just int of number of notes starting at note 0)
    plt.plot(order, pitch)
    plt.xlabel("Order")
    plt.ylabel("Pitch")
    plt.show()

# Primary function entry point of programm
def main():
    # Setup pin modes with functions, read the file
    setupPins()
    notes = doFileIO('song.txt' , singing)

    # Flag variable for if the reed switch is closed
    reedSwitchTriggerd = False
    
    #print(GPIO.input(switchPin))

    # If in singing mode check reed switch and graph
    if (singing == True):
      
        # As long as reed switch is closed check for state change
        while reedSwitchTriggerd == False:
            GPIO.input(switchPin)
            if (GPIO.input(switchPin)):
                reedSwitchTriggerd = True
                # Debounce
                time.sleep(1)

        # Clear global lists and for appending (used if programm ran multiple times without stopping)
        i = 0
        pitch.clear()
        duration.clear()
        order.clear()

        # Build the global arrays for graphing from each element in the returned 2D array and also play each note
        for note in notes:
            pitch.append(note[0])
            duration.append(note[1])
            order.append(i)
           # print (pitch[i], duration[i])

            # Play each note with buzz function defined above
            buzz(pitch[i], duration[i])
            i += 1

        # After playing song, plot the frequency of notes
        plotData()

    
# Surround programm in a try block for safe guarding  
try:
    main()


except(KeyboardInterrupt, SystemExit):
    print("Interrupt!")
    
finally:
    print("Done!")
 
    # Reset GPIO pins for next execution
    GPIO.cleanup()



