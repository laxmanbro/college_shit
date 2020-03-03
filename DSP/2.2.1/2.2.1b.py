import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-100, 100, 201)
y1 = (pow(.9, x1))*(np.heaviside(x1, 1))
y2 = np.sin(np.pi*(0.05)*x1)

plt.figure(1)
y3 = (pow(.9, -x1))*(np.heaviside(-x1, 1))
plt.stem(x1, y3)
plt.xlabel('$n$')
plt.ylabel('$y_1[n]=x_1[-n]$')
plt.grid()

#######################################
plt.figure(2)
y4 = np.sin(np.pi*(0.05)*(-x1))
plt.stem(x1, y4)
plt.xlabel('$n$')
plt.ylabel('$y_2[n]=x_2[-n]$')
plt.grid()
##################################################

plt.figure(3)
y5 = y1+y2
y6 = (((0.9)**(-x1))*(np.heaviside(-x1, 1)))+(np.sin(np.pi*(0.05)*(-x1)))
plt.stem(x1, y6)
plt.xlabel('$n$')
plt.ylabel('$y[n]$')
plt.grid()
##########################################

plt.figure(4)
y7 = ((0.9)**(-x1))*(np.heaviside(-x1, 1))+np.sin(np.pi*(0.05)*(-x1))
plt.stem(x1, y7)
plt.xlabel('$n$')
plt.ylabel('$y_1[n]+y_2[n]$')
plt.grid()
plt.show()

# same this can be done to all other functions which are defined in 2.1.1
