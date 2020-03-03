import numpy as np
import matplotlib.pyplot as plt

Fs = 500
x1 = np.linspace(-5, 5, Fs)

a=3
plt.figure(1)
y1=1/a*np.exp(-np.pi*x1*x1*1/a)

plt.plot(x1, y1)
plt.xlabel('0 < t < 4pi')
plt.ylabel('f1(t) = sin(nt)/n')

plt.grid()
plt.show()
