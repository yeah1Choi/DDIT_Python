# 첫 수를 입력하세요 :5
# 끝 수를 입력하세요 :6

# 5와 6의 합은 11입니다

sum = 0

firstInput = input("첫 수를 입력 : ")
secondInput = input("끝 수를 입력 : ")
# 입력값은 문자열!

firstNum = int(firstInput)
secondNum = int(secondInput)

sum = firstNum + secondNum

print(firstInput + "와 " + secondInput + "의 합은 " + str(sum) + "입니다.")

print("{}와 {}의 합은 {}입니다.".format(firstInput,secondInput,sum))
# format() : 타입과 상관없이 자동으로 집어넣음 *sum이 int임