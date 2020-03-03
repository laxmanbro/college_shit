import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
x1=np.linspace(-10,10,21)
y1=((0.95)**x1)*(np.heaviside(x1,1))
plt.stem(x1,y1)

plt.xlabel('$n$')
plt.ylabel('$x[n]$')

plt.legend()
plt.grid()

plt.figure(2)
y2=((0.95)**(-x1))*(np.heaviside(-x1,1))
plt.stem(x1,y2)

plt.xlabel('$n$')
plt.ylabel('$y[n]=x[-n]$')

plt.legend()
plt.grid()

plt.figure(3)
y3=(((0.95)**(x1))*(np.heaviside(x1,1)) + ((0.95)**(-x1))*(np.heaviside(-x1,1)))/2
plt.stem(x1,y3)

plt.xlabel('$n$')
plt.ylabel('$y[n]=\\frac{x[n]+x[-n]}{2}$')

plt.legend()
plt.grid()

plt.figure(4)
y4=(((0.95)**(x1))*(np.heaviside(x1,1)) - ((0.95)**(-x1))*(np.heaviside(-x1,1)))/2
plt.stem(x1,y4)

plt.xlabel('$n$')
plt.ylabel('$y[n]=\\frac{x[n]-x[-n]}{2}$')

plt.legend()
plt.grid()
plt.show()
