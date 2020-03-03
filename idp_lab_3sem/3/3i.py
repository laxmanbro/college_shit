import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of samplepoints
N = 2000
L =200
# sample spacing
Rtime = 1.0 / 800.0
#here u can vary Rtime anl L values by varying N and Rtime
n = np.linspace(0, N*Rtime, N)

y = np.cos(2*np.pi*n)+0.5*np.sin(4*np.pi*n)
#windowing done 
yf = scipy.fftpack.fft(y)

xf = np.linspace(-5, 1.0/(2.0*Rtime), N/2)
#here u can vary Rfreq and B by changing the linespace as shown above for frequency domain
yf1 = 2.0/N * np.abs(yf[:N//2])

plt.plot(xf, yf1)
plt.show()
