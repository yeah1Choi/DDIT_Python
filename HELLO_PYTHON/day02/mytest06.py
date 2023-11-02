# 출력할 단수를 입력하세요 :5
# 5 * 1 = 5
# 5 * 2 = 10
# ...
# 5 * 9 = 45

firstNum = int(input("출력할 단수를 입력하세요 : "))

print("** {}단 구구단 **".format(firstNum))

for i in range(1, 9+1):
    print("{} X {} = {}".format(firstNum, i, firstNum * i))