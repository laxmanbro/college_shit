import numpy as np
import matplotlib.pyplot as plt

x1=np.linspace(-10,10,21) #n
y1=((0.95)**x1)*(np.heaviside(x1,1)) #x[n]
M=10

y2=float(0)

for k in range(M+1):
	y2=y2+((0.95)**(x1-k))*(np.heaviside((x1-k),1)) #y_[n]


plt.figure(1)
plt.stem(x1,y2/M+1)
plt.xlabel('$n$')
plt.ylabel('$y[n]=\\frac{1}{M+1}\sum_{k=0}^{M}x[n-k]$')

plt.legend()
plt.grid()
plt.show()
