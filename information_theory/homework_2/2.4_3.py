import matplotlib.pyplot as plt
import numpy as np

p=np.linspace(0,1,1000)
h=[]

for i in p:
    h.append((-i)*(np.log2(i))-(1-i)*(np.log2(1-i)))


plt.plot(p,h)
plt.xlabel('p')
plt.ylabel('H(X)')
plt.grid()
plt.show()