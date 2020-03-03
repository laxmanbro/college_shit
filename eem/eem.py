import numpy as np
import matplotlib.pyplot as plt
# taking one dimentional arrayinstead og two dimentions
# taking the potential's along an arc which will be same radially(i.e. same along any arc)
# taking a 1 degree numpy arrays we have
arr = []
for x in range(45):
    arr.append(0.0)
arr[44] = 1.0
array1 = np.array(arr)
print(arr)
