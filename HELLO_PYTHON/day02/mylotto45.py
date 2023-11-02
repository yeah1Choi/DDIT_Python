from random import random

arr = list(range(0, 45+1))

# print(arr)

for i in range(1000):
    rnd = int(random()*46)
    
    temp = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = temp

print(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5])