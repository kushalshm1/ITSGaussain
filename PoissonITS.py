import numpy as np 
import matplotlib.pyplot as plt 
import math

sampleRate = 1000
n = 10
lm = 1.5
standardValueArray = []
valueArray = []

def probability(k): 
    return (math.exp(-lm)*(lm**k))/math.factorial(k)

#For Test Purpose:
# for x in range(1,10):
#     print(probability(x))

#Making the standard k array
i = 0
while(i<=n):
    standardValueArray.append(i)
    i = i+1

print(standardValueArray)

#Creating Frequency Array
frequencyArray = [0]*len(standardValueArray)
#Calculatig the K values for random probabilty
i = 0
while(i<sampleRate):
    randomProbability = np.random.rand()
    j = 0
    sum = 0
    while(sum<randomProbability):
        sum = sum + probability(j)
        j = j+1
    valueArray.append(j)
    i = i+1

valueArray.sort()
# print(valueArray)

#Calculating Frequency
i = 0
j = 0
while(i<sampleRate):
    if(valueArray[i]==standardValueArray[j]):
        frequencyArray[j] = frequencyArray[j]+1
    else:
        j = j+1
    i = i+1

print(frequencyArray)


plt.plot(standardValueArray,frequencyArray)
plt.show()
