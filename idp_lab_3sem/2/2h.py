import numpy as np
import matplotlib.pyplot as plt
from scipy import fft, arange
from scipy import signal


Fs = 1000
t = np.linspace(-2, 2, Fs)

#############################
plt.figure(1)
square = signal.square(2 * np.pi * t)


n = len(square)
k = arange(n)
T = n/Fs
frq = k/T
frq = frq[range(n/2)]
Y = fft(square)/n
Y = Y[range(n/2)]

plt.plot(frq, abs(Y))
plt.xlabel('-2 < t < 2')
plt.ylabel(' freq spectrum f1(t)')

########################

plt.figure(2)
triangle = 0.25-0.25*signal.sawtooth(2 * np.pi * t, 0.5)

n1 = len(triangle)
k1 = arange(n)
T1 = n/Fs
frq1 = k1/T1
frq1 = frq1[range(n1/2)]
Y1 = fft(triangle)/n1
Y1 = Y1[range(n/2)]

plt.plot(frq1, abs(Y1))
plt.xlabel('-2 < t < 2')
plt.ylabel(' freq spectrum f2(t)')


plt.grid()
plt.show()


plt.grid()
plt.show()
