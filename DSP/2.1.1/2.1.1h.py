import numpy as np
import matplotlib.pyplot as plt

x1=np.linspace(-10,10,210)
y2=np.sin((np.pi/4)*x1)-np.sin((np.pi/4)*(x1-1))
plt.stem(x1,y2)
plt.xlabel('$n$')
plt.ylabel('$x[n]-x[n-1]$')
plt.grid()
plt.show()
