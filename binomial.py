import numpy as np
import matplotlib.pyplot as plt
import math
#All the variables
p = 0.78
q = 1-p
N = 10
i = 0
arrProb = []
arrValue = []

def probability(K):
    return (math.factorial(N))/(math.factorial(N-K)*math.pow(p,K)*math.pow(q,(N-K)))

#Main Loop
while i<10000:
    K = np.random.binomial(N,p)
    arrProb.append(K)
    arrValue.append(probability(K))
    i = i+1


#Plotting
plt.scatter(arrProb,arrValue)
plt.show()




