import numpy as np
import matplotlib.pyplot as plt
# taking one dimentional arrayinstead og two dimentions
# taking the potential's along an arc which will be same radially(i.e. same along any arc)
# taking a 200 partition  numpy arrays we have

n = 200
print("taking ", n, " partitions  ")
size = len(np.linspace(0, np.pi/4, n))
V = np.zeros(size)
V[size-1] = 1
V[0] = 0
array = np.zeros(size)  # used in calculating error
err = []
err.append(1)
noi = 1
err1 = []
tolerance = 1e-6
while err[noi-1] > tolerance:
    for i in range(1, size-1):
        V[i] = (V[i-1]+V[i+1])/2.0
    # calculating error err in each iteration
    err.append(sum(abs(V[:] - array[:]))/size)
    array[:] = V[:]
    noi += 1
    err1.append(V[int(size/2)])  # V err1 at 22.5 deg

#############################################################

# plotting of v at 22.5 deg
n1 = range(1, noi)
plt.plot(n1, err1)
plt.xlabel('No. of iterations')
plt.ylabel('V($\pi$/8)')
plt.title('V($\pi$/8)')
plt.savefig(str(n)+'.jpg')
plt.show()

########################################################
# plotting error err1
n1 = range(1, noi+1)
plt.plot(n1, err)
plt.xlabel('No. of iterations')
plt.ylabel('Average error')
plt.title("Error")
axes = plt.gca()
axes.set_ylim([0, .0006])
plt.savefig('Error.jpg')
plt.show()

#################################################################################
print("The value of V(22.5 deg) derived from the analytical method = 0.5")
print("The value of V(22.5 deg) from numerical at last iteration is  = ",
      V[int(size/2)])
print("no. of iterations required to attain convergence is ~ 15000 for 200 partitions ant tolerance 1e-6")
#  no. of iterations required to attain convergence is ~ 15000.
