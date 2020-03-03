import numpy as np
import matplotlib.pyplot as plt

x1=np.linspace(-10,10,21)
y1=np.cos((np.pi/4)*x1)

y2=np.cos((np.pi/4)*x1)-np.cos((np.pi/4)*(x1-1))

plt.stem(x1,y2)
plt.xlabel('$n$')
plt.ylabel('$y[n]=x[n]-x[n-1]$')

plt.legend()
plt.grid()
plt.show()
