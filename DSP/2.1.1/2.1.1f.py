import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-10, 10, 210)  # n
y1 = np.cos((np.pi/4)*x1)  # x[n]
M = 10
y2 = 0.0
for k in range(M):
    y2 = y2+np.cos((np.pi/4)*(x1-k))  # y_[n]

plt.stem(x1, y2/(M+1))
plt.xlabel('n')
plt.ylabel('$y[n]=\\frac{1}{M+1}\sum_{k=0}^{M}x[n-k]$')
plt.grid()
plt.show()
