import math

f = open("file2.txt", "r")
if f.mode == "r":
    content = f.read()

# print(content)


each_char = [0.000]*256
count = 0

for i in content:
    count += 1
    p = ord(i)  # converts into ascii code of that character
    each_char[p] += 1

print "total ascii characters = " + str(count) 

for i in range(256):
    each_char[i] = each_char[i]/count

# print(each_char)

entropy = 0.00
for i in range(256):
    if(each_char[i] != 0):
        entropy = entropy+(each_char[i]*math.log(1/each_char[i], 2))


# final = {}
# final = each_char/count
# print(final)
# opt_size = 
print("entropy = "+str(entropy))
print ("compressed optimal size if iid in bytes = "+ str(count*entropy/8))
