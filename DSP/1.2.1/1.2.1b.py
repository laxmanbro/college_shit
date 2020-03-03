import numpy as np
import librosa
y, sr = librosa.load('audio.wav', sr=32000)  

# N = input("Enter the value of N(no. of bits) : ")
N = 4 #4 bit quantizer
length = 320000
arr = []
final1 = []
final2 = []
# print("Enter you array one by one ")
for x in range(length):
    arr.append(y[x])

b = arr[0]
for x in range(length):
    if arr[x] > b:
        b = arr[x]

a = arr[0]
for x in range(length):
    if arr[x] < a:
        a = arr[x]
count = 0
for x in arr:
    final1.append((x-a)/(b-a)*(pow(2, N)-1))
    final1[count] = int(final1[count])
    final2.append(final1[count]*(b-a)/(pow(2, N)-1)+a)
    # final2[count] = int(final2[count])
    count = count+1
fff = np.array(final2)

# print(final2)
librosa.output.write_wav('output_audio.wav', fff, sr)
