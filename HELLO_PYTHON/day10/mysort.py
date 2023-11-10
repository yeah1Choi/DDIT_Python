arr= [4,5,3,2,1]

for i in range(5):
    for j in range(5):
        if arr[i] < arr[j]:
            tempi = arr[i]
            tempj = arr[j]
            arr[i] = tempj
            arr[j] = tempi
            
print(arr)
            