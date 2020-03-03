import numpy as np
import matplotlib.pyplot as plt

# x1 = np.linspace(-10, 10, 21)
x = np.linspace(0, 100, 101)

h = np.sin((np.pi/4)*x)

x2 = (pow(0.999, x))
y = np.convolve(h, x2)
x1 = list(range(len(y)))

# print(x2)
# print(np.heaviside(x, 1))
plt.stem(x1, y)
plt.xlabel('$n$')
plt.ylabel('conv with sin ')
plt.grid()
plt.show()

# simililarly can be done with j
