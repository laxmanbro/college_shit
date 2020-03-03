import matplotlib.pyplot as plt
import numpy as np
import math
w = 4
h = 3
d = 70

plt.figure(figsize=(w, h), dpi=d)
x =np.array([-2,-1,0,1,2,3,4,5,6])
y =np.array([0.20725,0.174875,0.1363666,0.10175833,0.0701666,0.04455,0.0245166,0.010425,0.003975])

plt.xlabel('Eb/No in db')
plt.ylabel('Bit error rate')
plt.semilogy(x, y)
plt.show()
