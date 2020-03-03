import numpy as np
import matplotlib.pyplot as plt

A = np.array([-2,-2]) 
B = np.array([1,3]) 
C = np.array([4,-1]) 

a=np.linalg.norm(B-C)
b=np.linalg.norm(A-C)
c=np.linalg.norm(A-B)

W=(a*A+b*B)/(a+b)
print(W)
