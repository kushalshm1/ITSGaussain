import math
import numpy as np 
import matplotlib.pyplot as plt
import scipy
 
lm = 0.5
p=0
size = 1
# value = []
# probability = []
sumValue = []
proValue = []
def IP(k):    
    return ((math.exp(-lm)*(lm*k))/math.factorial(k))

# for z in range(1,100):
#     p = np.random.rand(1,1)
#     vl = IP(p)
#     probability[z] = p
#     value[z] = vl


# print(value)
# print(probability)
k = 0
count = 0
for z in range(0,1000):
    sum = 0
    k = 0
    # p = np.random.rand(1,1)
    while(sum<=p):
        p = np.random.poisson(lm,size)
        sum  =  sum  + IP(p)
        proValue.append(sum)
        sumValue.append(p)
        k = k+1
        count+=1
print(len(sumValue),count)
# print(sumValue)
# print(proValue)
testarr = [0]*len(proValue)

plt.scatter(sumValue,proValue)
plt.show()


