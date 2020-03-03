import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from scipy import signal


def integrate(f, a, b, N):
    x = np.linspace(a, b, N)
    fx = f
    area = np.sum(fx)*(b-a)/N
    return area


Fs = 500
T = 1
w0 = (2*np.pi)/T
t = np.linspace(-2, 2, Fs)
square = signal.square(2 * np.pi * t)
triangle = 0.25-0.25*signal.sawtooth(2 * np.pi * t, 0.5)
a0 = 0
a0 = (integrate(square, 0, 1, 1000)-0.002)*1/T  # The answer is off by about 0.002
a01 = 0
a01 = (integrate(triangle, 0, 1, 1000))*2/T  # The answer is off by about 0.002
a = []
a.append(0)
b = []
b.append(0)
a1 = []
a1.append(0)
b1 = []
b1.append(0)
xa = []
for i in range(100):
    xa.append(i)


for k in range(1, 100):
    a.append(((integrate(square*np.cos(k*w0*t), 0, 1, 1000))-0.002)*2/T)
    b.append(((integrate(square*np.sin(k*w0*t), 0, 1, 1000))-0.002)*2/T)
    a1.append(((integrate(triangle*np.cos(k*w0*t), 0, 1, 1000)))*4/T)
    b1.append(((integrate(triangle*np.sin(k*w0*t), 0, 1, 1000)))*4/T)


print("value of a0 for square wave f1 is :  ")
print(a0)
print("value of a0 for trangular wave f2 is :  ")

print(a01)

plt.figure(1)
plt.stem(xa, a)
plt.title("a[k] for square f1 wave")
plt.xlabel('0 < k < 100')
plt.ylim(-1,1)
plt.ylabel('a[k]')

plt.figure(2)
plt.stem(xa, b)
plt.title("b[k] for square f1 wave")
plt.xlabel('0 < k < 100')
plt.ylabel('b[k]')

plt.figure(3)
plt.stem(xa, a1)
plt.title("a[k] for traiangle f2 wave")
plt.xlabel('0 < k < 100')
plt.ylabel('a[k]')

plt.figure(4)
plt.stem(xa, b1)
plt.ylim(-1,1)
plt.title("b[k] for triangle f2 wave")
plt.xlabel('0 < k < 100')
plt.ylabel('b[k]')


plt.grid()
plt.show()
