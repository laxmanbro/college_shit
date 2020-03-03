import math
import random
import numpy

print("enter number of trails")
num_trails = int(input())

arr=[]

y=0
for y in range(num_trails):
    x = numpy.random.rand()
    if(x<0.5):
        x = 0
    else:
        x = 1
    arr.append(x)
 
print("the random numbers are : " )
print(arr)



