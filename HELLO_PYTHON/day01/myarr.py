arr = ["홍길동","전우치","이순신"]

print(arr)
arr.append("홍범도")
print(arr)
arr.insert(len(arr), "도요토미")
print(arr)

print(arr[0])

print(arr[-2]) 
# -를 넣으면 역순으로 배열을 출력

# print(arr[-6]) 
# 역순을 넘은 -수를 넣으면 에러!