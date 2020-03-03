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

xa = []
for i in range(100):
    xa.append(i)

a = []
b = []
print(complex)

for k in range(0, 100):
    a.append(((integrate(square*np.exp(-k*w0*t*complex(0, 1)), 0, 1, 1000))-0.002)*1/T)
    b.append(((integrate(triangle*np.exp(-k*w0*t*complex(0, 1)), 0, 1, 1000)))*2/T)


print("ck for f1 square wave")
print(a)
print("ck for f2 triangle wave")
print(b)
