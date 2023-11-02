# 첫 수를 입력하세요 :1
# 끝 수를 입력하세요 :6
# 배수를 입력하세요 :3

# 1에서 6까지의 3의 배수의 합은 9입니다.

firstInput = input("첫 수를 입력하세요 : ")
secondInput = input("끝 수를 입력하세요 : ")
thirdInput = input("배수를 입력하세요 : ")

firstNum = int(firstInput)
secondNum = int(secondInput)
thirdNum = int(thirdInput)

sum = 0
arr = list(range(firstNum, secondNum+1))

for i in arr:
    if 0 == (i % thirdNum):
        sum += i
    
print("{}에서 {}까지의 {}의 배수의 합은 {}입니다.".format(firstNum,secondNum,thirdNum,sum))