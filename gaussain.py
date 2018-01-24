import math #importing Mathematics library
import numpy as np #importing numpy
import matplotlib as pyplot #importing matplotlib

size = 30 #number of bins

mu = 0 #Mean
sigma = 1 #Standard Deviation 

maxima = 3.4 #maximum value 

minsigma = mu - maxima #Minimum value | Assuming mean to be 0

maxsigma = mu + maxima #Maximum value | Assuming mean to be zero
divSize = 8/size #Bin Size

arr = [0]*size #Creating a list with "Size" number of items filled with 0

for y in range(1,1000):
    x = np.random.normal(mu ,sigma)  #Values of Relative Frequencies from Normal Probability Distribution
    k =(len(arr)-1) - math.floor( (maxsigma-x)/divSize ) #Getting the value of index
    k = int(k) #Converting the value of index to Integer Data Type | Truncating
    arr[k] = arr[k]+1 #Incrementing +1 on values of k to its respective indices

print(arr) #Printing the final array which contains values drawn from Normal Distribution





