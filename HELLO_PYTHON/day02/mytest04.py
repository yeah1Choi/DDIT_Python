# 홀/짝을 고르시오
# 0.5보다 크면 홀수 작으면 짝수

# 나: 홀
# 컴: 홀

# 결과: 같으면 승 / 다르면 패

from random import random

myDes = input("홀/짝을 고르시오 : ")

comInput = random()

print("comInput", comInput)

comDes = ""

if comInput > 0.5 :
    comDes = "홀"
else :
    comDes = "짝"

result = ""

if myDes == comDes :
    result = "승리 ~"
else :
    result = "패배 ㅠㅠ"
    
print("나는 {}, 컴퓨터는 {} => 당신은 {}".format(myDes, comDes, result))