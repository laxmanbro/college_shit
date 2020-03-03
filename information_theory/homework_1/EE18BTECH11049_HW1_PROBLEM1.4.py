import matplotlib.pyplot as plt
import numpy as np


def f_inverse(x):
    if(x < 0.1):
        return 0
    elif(x < 0.4 and x >= 0.1):
        return 1
    elif(x < 0.5 and x >= 0.4):
        return 2
    elif(x < 1 and x >= 0.5):
        return 3
    elif(x == 1):
        return 3


# x = np.arange(0., 1., 0.01)

y = []


for x in range(10):

    x1 = np.random.rand()
    y.append(f_inverse(x1))


print(y)





