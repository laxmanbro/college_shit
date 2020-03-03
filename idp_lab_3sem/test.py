import numpy as np
import matplotlib.pyplot as plt
from scipy import fft, arange
from scipy import signal


Fs = 1000
t = np.linspace(-2, 2, Fs)

#############################
plt.figure(1)
square = signal.square(2 * np.pi * t)
print(square)