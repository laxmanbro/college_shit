import numpy as np
import matplotlib.pyplot as plt

Fs = 8000.0
x1 = np.linspace(-15, 15, 31)


plt.figure(1)
f1 = 1000.0
y1 = np.cos((2 * np.pi*f1/Fs)*x1)
plt.stem(x1, y1)
plt.grid()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
#####################################

plt.figure(2)
f2 = 2000.0
y2 = np.cos((2*np.pi*f2/Fs)*x1)
plt.stem(x1, y2)
plt.grid()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
####################################

plt.figure(3)
f3 = 3000.0
y3 = np.cos((2*np.pi*f3/Fs)*x1)
plt.stem(x1, y3)
plt.grid()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
##########################################

plt.figure(4)
f3_5 = 3500.0
y3_5 = np.cos((2*np.pi*f3_5/Fs)*x1)
plt.stem(x1, y3_5)
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
plt.grid()
#################################

plt.figure(5)
f4 = 4000.0
y4 = np.cos((2*np.pi*f4/Fs)*x1)
plt.stem(x1, y4)
plt.grid()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
###################################

plt.figure(6)
f5 = 5000.0
y5 = np.cos((2*np.pi*f5/Fs)*x1)
plt.stem(x1, y5)
plt.grid()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
################################

plt.figure(7)
f6 = 6000.0
y6 = np.cos((2*np.pi*f6/Fs)*x1)
plt.stem(x1, y6)
plt.grid()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
######################################

plt.figure(8)
f7 = 7000.0
y7 = np.cos((2*np.pi*f7/Fs)*x1)
plt.stem(x1, y7)
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
plt.grid()


plt.show()
