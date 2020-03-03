import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(-N*T, N*T, N)
y = np.exp(x*x * -np.pi)
yf = scipy.fftpack.fft(y)
xf = np.linspace(-5, 1.0/(2.0*T), N/2)
yf1 = 2.0/N * np.abs(yf[:N//2])

plt.plot(xf, yf1)
plt.xlim(-50, 50)
plt.show()
