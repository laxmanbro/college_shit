import numpy as np
import matplotlib.pyplot as plt

Fs = 500
x1 = np.linspace(-20, 20, Fs)

plt.figure(1)
y1=np.exp(-np.pi*x1*x1)

plt.plot(x1, y1)
plt.xlabel('0 < t < 4pi')
plt.ylabel('f1(t) = sin(nt)/n')

plt.grid()
plt.show()
