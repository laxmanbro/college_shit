import numpy as np
import matplotlib.pyplot as plt

x1=np.linspace(-10,10,21) #n
y1=((0.95)**x1)*(np.heaviside(x1,1))   #x_[n]

y2=((0.95)**x1)*(np.heaviside(x1,1))-((0.95)**(x1-1))*(np.heaviside((x1-1),1)) #y[n]=x[n]-x[n-1]
y3=((0.95)**x1)*(np.heaviside(x1,1))-(2*(((0.95)**(x1-1))*(np.heaviside((x1-1),1))))+((0.95)**(x1-2))*(np.heaviside((x1-2),1)) #y[n]=x[n]-2x[n-1]+x[n-2]

plt.figure(1)
plt.stem(x1,y2)
plt.xlabel('$n$')
plt.ylabel('$y[n]=x[n]-x[n-1]$')

plt.legend()
plt.grid()

plt.figure(2)

plt.stem(x1,y3)
plt.xlabel('$n$')
plt.ylabel('$y[n]=x[n]-2x[n-1]+x[n-2]$')

plt.legend()
plt.grid()
plt.show()
