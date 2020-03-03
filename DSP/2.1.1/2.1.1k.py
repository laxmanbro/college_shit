import numpy as np
import matplotlib.pyplot as plt

x1=np.linspace(-10,10,210)
y1=np.sin((np.pi/4)*x1)
y11=(np.sin((np.pi/4)*x1))**2
plt.stem(x1,y11)
plt.xlabel('$n$')
plt.ylabel('$y[n]=x^2$')
plt.grid()
plt.show()
