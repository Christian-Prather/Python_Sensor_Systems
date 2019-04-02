import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.csv', delimiter= ',' )
print (data)

time = data[0]
cheese = data[1]
time = [int(i) for i in time]  # This is a method to combine for and casting utilizing list comprehension

plt.title("Too Much Cheese") # Title of plt

plt.plot(time, cheese) # Plot axis

ax = plt.gca() # Create reference to plt named ax
ax.set_xlabel("Time in Years") # X axis 
ax.set_ylabel("Lbs of Cheese")

plt.savefig("Cheese.pdf") # Export pdf
plt.show() # Show the graph

# Generate a dictionary of the two lists
keys = cheese
values = time
d = dict(zip(keys, values)) # creates a directory from two variables ("zip") 
print (d) # Output dictionary for debug

sortedList = sorted(d.items(), reverse = True) # Sort the dictionary for the max value in decending order
max = sortedList[0] # Store max value as variable max
print(max)

# Display data nicely
print("In", str(d[max[0]]) +" "+ str(max[0]),"lbs of cheese was consumed, daaaannnngggg")