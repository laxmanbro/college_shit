#question no.6

import numpy as np
import matplotlib.pyplot as plt
import math


def unitVec(X):
	temp1=math.sqrt(X[0]*X[0]+X[1]*X[1])
	p=np.zeros(2)
	p[0]=X[0]/temp1
	p[1]=X[1]/temp1
	return p

def norm_vec(Y):
	return np.matmul(omat,Y)

omat=np.array([[0,1],[-1,0]])
	
normalDir_AB= np.array([1,-1])
normalDir_AD = np.array([7,-1]) 

vecDir_AB=norm_vec(normalDir_AB)
vecDir_AD=norm_vec(normalDir_AD)

mag=math.sqrt(normalDir_AB[0]*normalDir_AB[0]+normalDir_AD[1]*normalDir_AD[1])

dir_AC=(unitVec(vecDir_AB)+unitVec(vecDir_AD))*mag
dir_DB=norm_vec(dir_AC)	


ZZ=np.vstack((dir_AC,[1,0]))
XX=np.vstack((dir_DB,[1,0]))

Q=np.linalg.inv(ZZ)
W=np.array([-6,0])
A=np.dot(Q,W)
print(A)

E=np.linalg.inv(XX)
R=np.array([0,0])
B=np.dot(E,R)
print(B,' : This is origin , so it is not considered in answer')
