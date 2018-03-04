import matplotlib.pyplot as plt
import numpy as np 
import math

N = 10
p = 0.765
q = 1-p
sampleRate = 1000
standardValueArray = []
valueArray = []
def probability(k):
    one = (math.factorial(N)/(math.factorial(N-k)*math.factorial(k)))
    two = ((p**k)*(q**(N-k)))
    three = one*two
    return three

#For test purposes
# for x in range(1,10):
    # print(probability(x))

i = 0
while(i<=N):
    standardValueArray.append(i)
    i = i+1
print(standardValueArray)
frequencyArray = [0]*len(standardValueArray)

#Filling Values of K into valueArray
i = 0
while(i<sampleRate):
    j = 0
    add = 0
    random = np.random.rand()
    while(add<random):
        add = add + probability(j)
        j = j+1
    j = j-1
    valueArray.append(j)
    i = i+1

valueArray.sort()
# print(valueArray)
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
