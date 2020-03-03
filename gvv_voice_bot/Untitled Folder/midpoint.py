import numpy as np 
import matplotlib.pyplot as plt 

def mid_pt(x,y):
	return((x+y)/2)

A=np.matrix('-2;-2')
B=np.matrix('1;3')
C=np.matrix('4;-1')

print(mid_pt(B,C))
print(mid_pt(A,B))
print(mid_pt(A,C))

