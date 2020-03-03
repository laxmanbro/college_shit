import numpy as np
import matplotlib.pyplot as plt
from scipy import fft, arange
Fs = 1000
x1 = np.linspace(-8*np.pi, 8*np.pi, 1000)

#############################
plt.figure(1)
N = int(input("enter value of N : "))
y1 = 0
for n in range(1, N+1, 1):
    y1 = y1 + (np.sin(n*x1)/n)

n = len(y1)
k = arange(n)
T = n/Fs
frq = k/T
frq = frq[range(n/2)]
Y = fft(y1)/n
Y = Y[range(n/2)]

plt.plot(frq, abs(Y))
plt.xlabel('0 < t < 4pi')
plt.ylabel(' freq spectrum f2(t)')

plt.grid()
plt.show()
