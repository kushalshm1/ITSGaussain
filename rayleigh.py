import math
import numpy as np 
import matplotlib.pyplot as plt

lm = 0.5
i=0
x=5
valueProb = [0]
valueRV = [0]

def probablity(mode):
    return (2*x*math.exp(-lm**2/mode))/mode



while(i<1000):
    p=np.random.rayleigh(1,1)
    valueRV.append(p) 
    print(p)
    valueProb.append(probablity(p))
    i = i+1

print(valueRV)
print(valueProb)
plt.scatter(valueRV,valueProb)
plt.show()
