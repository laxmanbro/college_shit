N = input("Enter the value of N(no. of bits) : ")
length = input("Enter the length of array : ")
arr = []
final1 = []
final2 = []
print("Enter you array one by one ")
for x in range(length):
    arr.append(input())

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
    final1 = int(final1)
    final2.append(final1[count]*((b-a)/(pow(2, N)-1))+a)
    count = count+1

print(final2)
