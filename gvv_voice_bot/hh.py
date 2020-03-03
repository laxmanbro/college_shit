import numpy as np 
import matplotlib.pyplot as plt 
A=np.array([-2,-2])
B=np.array([1,3])
len=10
x_AB=np.zeros((2,len))
lam_1 =np.linspace(0,1,len)
for i in range(len):
	temp1=A+lam_1[i]*(B-A)
	x_AB[:,i]=temp1.T 

print(x_AB)