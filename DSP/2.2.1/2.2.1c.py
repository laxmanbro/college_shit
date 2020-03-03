import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-100, 100, 201)

plt.figure(1)
y1 = ((0.9)**x1)*(np.heaviside(x1, 1))
plt.stem(x1, y1)
plt.xlabel('$n$')
plt.ylabel('$x1[n]$')
plt.grid()
############################################

plt.figure(2)
y3 = ((0.9)**(-x1))*(np.heaviside(-x1, 1))
plt.stem(x1, y3)
plt.xlabel('$n$')
plt.ylabel('$y1[n]=x1[-n]$')
plt.grid()
######################################

plt.figure(3)
y2 = np.sin(np.pi*(0.05)*x1)
plt.stem(x1, y2)
plt.xlabel('$n$')
plt.ylabel('$x2[n]$')
plt.grid()
#################################

plt.figure(4)
y4 = np.sin(np.pi*(0.05)*(-x1))
plt.stem(x1, y4)
plt.xlabel('$n$')
plt.ylabel('$y2=x_2[-n]]$')
plt.grid()

######################################
plt.figure(5)
y5 = ((0.9)**(x1-5))*(np.heaviside((x1-5), 1)) 
plt.stem(x1, y5)
plt.xlabel('$n$')
plt.ylabel('$x1[n-5]$')
plt.grid()

###########################################
plt.figure(6)
y7 = ((0.9)**(5-x1))*(np.heaviside((5-x1), 1)) 
plt.stem(x1, y7)
plt.xlabel('$n$')
plt.ylabel('$y1[n1]=x1[5-n]$')
plt.grid()

######################################
plt.figure(7)
y6 = np.sin(np.pi*(0.05)*(x1-5))  
plt.stem(x1, y6)
plt.xlabel('$n$')
plt.ylabel('$x2[n-5]$')
plt.grid()

###################################
plt.figure(8)
y8 = np.sin(np.pi*(0.05)*(5-x1)) 
plt.stem(x1, y8)
plt.xlabel('$n$')
plt.ylabel('$y1[n1]=x2[n-5]$')
plt.grid()
plt.show()


# same this can be done to all other functions which are defined in 2.1.1
