import numpy as np
import matplotlib.pyplot as plt

x1=np.linspace(-10,10,210)
y1=np.sin((np.pi/4)*(x1-2))+np.sin((np.pi/4)*(2-x1))
plt.stem(x1,y1)
plt.xlabel('$n$')
plt.ylabel('$y[n]=x[n-2]+x[2-n]$')
plt.grid()
plt.show()
