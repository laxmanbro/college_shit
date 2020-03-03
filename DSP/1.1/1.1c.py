import numpy as np
import matplotlib.pyplot as plt

Fs = 8000.0
Fs1 = 80000.0
x1 = np.linspace(-5, 5, 11)
x2 = np.linspace(-5, 5, 110)


plt.figure(1)
f1 = 1000.0
y1 = np.cos((2 * np.pi*f1/Fs)*x1)
y11 = np.cos((2 * np.pi*f1/Fs)*x2)

plt.stem(x1, y1, 'r', label='x[n]')
plt.stem(x2, y11, 'b', label='y[n]')

plt.grid()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
plt.legend()
#####################################

plt.figure(2)
f2 = 2000.0
y2 = np.cos((2*np.pi*f2/Fs)*x1)
y21 = np.cos((2 * np.pi*f2/Fs)*x2)

plt.stem(x1, y2, 'r', label='x[n]')
plt.stem(x2, y21, 'b', label='y[n]')

plt.grid()
plt.legend()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
####################################

plt.figure(3)
f3 = 3000.0
y3 = np.cos((2*np.pi*f3/Fs)*x1)
y31 = np.cos((2 * np.pi*f3/Fs)*x2)

plt.stem(x1, y3, 'r', label='x[n]')
plt.stem(x2, y31, 'b', label='y[n]')

plt.grid()
plt.legend()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
##########################################

plt.figure(4)
f3_5 = 3500.0
y3_5 = np.cos((2*np.pi*f3_5/Fs)*x1)
y3_51 = np.cos((2 * np.pi*f3_5/Fs)*x2)

plt.stem(x1, y3_5, 'r', label='x[n]')
plt.stem(x2, y3_51, 'b', label='y[n]')

plt.xlabel('n')
plt.legend()
plt.ylabel('x[n] = sin(n)')
plt.grid()
#################################

plt.figure(5)
f4 = 4000.0
y41 = np.cos((2 * np.pi*f4/Fs)*x2)

y4 = np.cos((2*np.pi*f4/Fs)*x1)
plt.stem(x1, y4, 'r', label='x[n]')
plt.stem(x2, y41, 'b', label='y[n]')
plt.legend()
plt.grid()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
###################################

plt.figure(6)
f5 = 5000.0
y51 = np.cos((2 * np.pi*f5/Fs)*x2)

y5 = np.cos((2*np.pi*f5/Fs)*x1)
plt.stem(x1, y5, 'r', label='x[n]')
plt.stem(x2, y51, 'b', label='y[n]')
plt.legend()
plt.grid()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
################################

plt.figure(7)
f6 = 6000.0
y61 = np.cos((2 * np.pi*f6/Fs)*x2)

y6 = np.cos((2*np.pi*f6/Fs)*x1)
plt.stem(x1, y6, 'r', label='x[n]')
plt.stem(x2, y61, 'b', label='y[n]')

plt.grid()
plt.legend()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
######################################

plt.figure(8)
f7 = 7000.0
y71 = np.cos((2 * np.pi*f7/Fs)*x2)

y7 = np.cos((2*np.pi*f7/Fs)*x1)
plt.stem(x1, y7, 'r', label='x[n]')
plt.stem(x2, y71, 'b', label='y[n]')
plt.legend()
plt.xlabel('n')
plt.ylabel('x[n] = sin(n)')
plt.grid()


plt.show()
