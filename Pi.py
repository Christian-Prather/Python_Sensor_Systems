from math import *

runLength = int(input ("Please enter selected amount of times for summation ")) #amount of times to use in sigma
summation = 0
intermediate = 0 # value for temp data storage for easier reading
scalar = (2*(sqrt(2))/9801) 

# for 1 - userchosen range run calcualtions
for i in range(runLength + 1):
    #print("Hey") # Debug
    intermediateNumerator = factorial(4*i) * (1103 + (26390 * i))
    #print(intermediateNumerator)  # Debug
    intermediateDenominator =  (factorial(i)**4) * (396**(4*i))
    #print(intermediateDenominator)  # Debug
    intermediate = intermediateNumerator/ intermediateDenominator
    #print (intermediate)  # Debug
    summation += intermediate
    #print (summation)  # Debug
summation = 1/ (scalar * summation)
print("Final:", summation)
print("Actual:", pi)

#calculate percent error of aproximation 
#Yields 0%
percentError = abs((summation - pi)/ pi) * 100
print(percentError)


####################################################################################
# Calcualtion of exponential 
calculatedExpenential = 0
valueToUse = int(input("Value to use: ")) # value to raise e to e^valueToUse
runLength = int(input ("Please enter selected amount of times for summation ")) # Number of sigma additions to run

# run calculations runLength amount of time
for i in range(runLength + 1):
    intermediateExpenential = (valueToUse ** i) / factorial(i)
    calculatedExpenential += intermediateExpenential 

print("Final", calculatedExpenential)
print("Actual:", exp(valueToUse))

# calcualte percent error 
# runLength > 10 yields 0%
percentError = abs((calculatedExpenential - exp(valueToUse))/ exp(valueToUse)) * 100
print(percentError)



