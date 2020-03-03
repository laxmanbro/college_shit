import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 500
t = np.linspace(-2, 2, Fs)
square =signal.square(2 * np.pi  * t)
plt.figure(1)
plt.plot(t, square)
plt.xlabel('-2 < t < 2')
plt.ylabel('f1(t) = sin(nt)/n')
plt.ylim(-2,2)


##############################################
plt.figure(2)

triangle = 0.25-0.25*signal.sawtooth(2 * np.pi * t, 0.5)
plt.plot(t, triangle)
plt.grid()
plt.ylim(-1, +1)
plt.show()


