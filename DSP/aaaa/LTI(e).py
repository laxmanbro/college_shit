import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
x1=np.linspace(-10,10,21)
y1=np.cos((np.pi/4)*x1)
plt.stem(x1,y1)

plt.xlabel('$n$')
plt.ylabel('$x[n]$')

plt.legend()
plt.grid()

plt.figure(2)
y2=np.cos((np.pi/4)*(x1-5))
plt.stem(x1,y2)

plt.xlabel('$n$')
plt.ylabel('y[n]=x[n-5]')

plt.legend()
plt.grid()
plt.show()
