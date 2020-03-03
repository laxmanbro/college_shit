import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
x1 = np.linspace(-15, 15, 31)
u = np.heaviside(x1, 1)
u1 = np.heaviside(-x1, 1)
y1 = ((0.95)**x1)*u
plt.stem(x1, y1)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid()

#########################
plt.figure(2)
y2 = ((0.95)**(-x1))*u1
plt.stem(x1, y2)
plt.xlabel('n')
plt.ylabel('x[-n]')
plt.grid()

#################################
plt.figure(3)
y3 = ((pow(.95, x1))*u +
      (pow(.95, -x1))*u1)/2
plt.stem(x1, y3)
plt.xlabel('n')
plt.ylabel('x[n]+x[-n] /2')
plt.grid()

#################################
plt.figure(4)
y4 = ((pow(.95, x1))*u -
      (pow(.95, -x1))*u1)/2
plt.stem(x1, y4)
plt.xlabel('n')
plt.ylabel('x[n]-x[-n] /2')
plt.grid()


plt.show()
