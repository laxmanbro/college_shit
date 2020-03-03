import numpy as np
import matplotlib.pyplot as plt
Fs = 1000
x1 = np.linspace(0, 4*np.pi, Fs)


plt.figure(1)
N = int(input("enter value of N : "))
y1 = 0
for n in range(1, N+1):
    y1 = y1 + (np.sin(n*x1)/n)

plt.plot(x1, y1)
plt.xlabel('-4pi < t < 4pi')
plt.ylabel('f1(t) = sin(nt)/n')

plt.grid()
plt.show()
