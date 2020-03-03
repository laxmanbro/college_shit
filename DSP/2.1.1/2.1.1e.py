import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
x1 = np.linspace(-15, 15, 310)
y1 = np.sin((np.pi/4)*x1)
plt.stem(x1, y1)
plt.xlabel('n')
plt.title("sin[n]")
plt.ylabel('x[n]')
plt.grid()
#########################

plt.figure(2)
y2 = np.sin((np.pi/4)*(x1-5))
plt.stem(x1, y2)
plt.xlabel('n')
plt.title("sin[n-5]")
plt.ylabel('x[n-5]')
plt.grid()

########################
plt.show()
