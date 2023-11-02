# 첫 수를 입력하세요 :1
# 끝 수를 입력하세요 :4

# 1에서 4까지의 합은 10입니다.

firstInput = input("첫 수를 입력하세요 : ")
secondInput = input("끝 수를 입력하세요 : ")

firstNum = int(firstInput)
secondNum = int(secondInput)

sum = 0

for i in range(firstNum, secondNum+1):
    sum += i

print("{}에서 {}까지의 합은 {}입니다.".format(firstNum, secondNum, sum))