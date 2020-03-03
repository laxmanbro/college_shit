import numpy as np
import matplotlib.pyplot as plt

# x1 = np.linspace(-10, 10, 21)
x = np.linspace(-10, 10, 21)
f = 0.0
M = 10
for k in range(M):
    f = f + np.heaviside(x-k, 1) - np.heaviside(x-(1+k), 1)
h1 = float(0)
h = h1+(f/(M+1))

x2 = (pow(0.95, x))*(np.heaviside(x, 1))
y = np.convolve(h, x2)
x1 = list(range(len(y)))

# print(x2)
# print(np.heaviside(x, 1))
plt.stem(x1, y)
plt.xlabel('$n$')
plt.ylabel('$y[n]=\sum_{k=-\infty}^{\infty}x[k]h[n-k]$')
plt.grid()
plt.show()

# simililarly can be done with j
