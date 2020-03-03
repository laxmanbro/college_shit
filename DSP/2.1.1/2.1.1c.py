import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-15, 15, 31)

plt.figure(1)
y1 = np.sin((np.pi/4)*x1)
plt.stem(x1, y1)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title("sin[n]")
plt.grid()
##################################
plt.figure(2)
y2 = (np.sin((np.pi/4)*x1)-np.sin((np.pi/4)*(-x1)))/2
plt.stem(x1, y2)
plt.title("odd od sin[n]")
plt.xlabel('n')
plt.ylabel('(x[n]-x[-n])/2')
plt.grid()
################################
plt.show()
