import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100, 100, 201)

plt.figure(1)
y1 = ((0.9)**x)*(np.heaviside(x, 1))
plt.stem(x, y1)
plt.xlabel('$n$')
plt.ylabel('$x[n]$')
plt.grid()

######################################

plt.figure(2)
y2 = np.sin(np.pi*(0.05)*x) 
plt.stem(x, y2)
plt.xlabel('$n$')
plt.ylabel('$x2[n]$')
plt.grid()


plt.show()
