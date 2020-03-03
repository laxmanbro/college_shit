import numpy as np
import math
# from scipy import special

from matplotlib import pyplot as plt
monalisa = np.load("mss.npy")
plt.imshow(monalisa, 'gray')
# plt.show()python


mona_arr = []
for i in range(400):  # changing as 1D array
    for j in range(300):
        mona_arr.append(monalisa[i][j])
mona_ar = np.array(mona_arr)


ch_enc_arr = []

# print(mona_ar)
for i in range(120000):
    ch_enc_arr.append(mona_ar[i])
    ch_enc_arr.append(mona_ar[i])
    ch_enc_arr.append(mona_ar[i])


# print(ch_enc_arr)
ch_enc_arr = np.array(ch_enc_arr)

# print(ch_enc_arr)


ch_enc_arr = -2*ch_enc_arr+1  # x to +1 or -1 conversion


# print(mona_ar)
# t = np.arange(0, 0.0055, 0.000001/50)

fc = 2000000.00  # carrier frequency
Ts = 1/50000000.00  # sampling time
St = []

# print(St[2])
n = 0


for i in range(180000):  # defining S(t)
    for j in range(50):
        St.append(ch_enc_arr[2*i]*np.cos(2*np.pi*fc*n*Ts) +
                  ch_enc_arr[2*i+1]*np.sin(2*np.pi*fc*n*Ts))
        n = n+1

# print n
St_arr = np.array(St)

# St_square = St_arr*St_arr
# Eb = np.sum(St_square)/(2*5500)

T = 0.000001
n = 3.00
k = 1.00
Eb = T/2.00*n/k  # energy per bit
# prit Eb
x = 4.00  # Eb/No in decibels

std = np.sqrt(Eb*1/Ts*0.5*pow(10.00, -x/10.00))  # standard deviation


# St_arr = St_arr*St_arr
# sum = np.sum(St_arr)
# print(sum)
samples = np.random.normal(0, std, 180000*50)  # white gaussian noise

rt = St_arr + samples   # recived signal

# print(rt)


def z1(n):  # 4-QAM constellations
    return (np.cos(2*np.pi*fc*n*Ts) + np.sin(2*np.pi*fc*n*Ts))


def z2(n):
    return (-np.cos(2*np.pi*fc*n*Ts) + np.sin(2*np.pi*fc*n*Ts))


def z3(n):
    return (-np.cos(2*np.pi*fc*n*Ts) - np.sin(2*np.pi*fc*n*Ts))


def z4(n):
    return (np.cos(2*np.pi*fc*n*Ts) - np.sin(2*np.pi*fc*n*Ts))


countZ1 = 0
countZ2 = 0
countZ3 = 0
countZ4 = 0

n = 0
new_arr = []


for j in range(180000):
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    for i in range(50):
        a1 = a1 + (rt[n]-z1(n))**2
        # print((rt[n]-z1(n))**2)
        # print(a1)
        a2 = a2 + (rt[n]-z2(n))**2
        a3 = a3 + (rt[n]-z3(n))**2
        a4 = a4 + (rt[n]-z4(n))**2
        n = n+1

    d1 = np.sqrt(a1)
#     print d1
    d2 = np.sqrt(a2)
    d3 = np.sqrt(a3)
    d4 = np.sqrt(a4)

    min_dist = min([d1, d2, d3, d4])  # minimum distance calculation

#     print min_dist

    if min_dist == d1:
        new_arr.append(1)
        new_arr.append(1)
    elif min_dist == d2:
        new_arr.append(-1)
        new_arr.append(1)
    elif min_dist == d3:
        new_arr.append(-1)
        new_arr.append(-1)
    else:
        new_arr.append(1)
        new_arr.append(-1)


# print(new_arr)

new = np.array(new_arr)
new_arr = (new-1)/-2

# print len(new_arr)


# rows, cols = (110, 100)
# ans_arr = [[0]*cols]*rows
# p = 0

# print(new_arr)


final_arr = []
# print ch1
puppy = 0
for i in range(120000):
    x1 = new_arr[puppy]
    x2 = new_arr[puppy+1]
    x3 = new_arr[puppy+2]
    puppy = puppy + 3
    if (x1+x2+x3 == 0) or (x1+x2+x3 == 1):
        final_arr.append(0)
    else:
        final_arr.append(1)


# print(final_arr)

# print np.bitwise_xor(ch1, x)
final_arr = np.array(final_arr)


d = final_arr.reshape(400, 300)


# final = np.array(ans_arr)

# print(final.size)
# ffff = (final-1)/-2

plt.imshow(d, 'gray')
plt.show()

monalisaaaa = np.load("mss.npy")
y = d - monalisaaaa
y[y < 0] = 1
print np.sum(y)  # BER*11000

# print math.erfc((2.00*pow(10.00, x/10.00))/np.sqrt(2.00))/2.00

# print(np.sqrt(sum))
