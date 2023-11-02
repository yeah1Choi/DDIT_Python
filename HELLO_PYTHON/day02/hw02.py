# 컴 :50(안보임)    *1~99 사이의 랜덤 수
# 나 :40
# 컴 :더 큰 수입니다
# 나 :60
# 컴 :더 작은 수입니다
# 나 :50
# 컴 :정답입니다~     *최대 10번의 기회
from random import random

comAnswer = int(random()*99)+1 

print("comAnswer",comAnswer)

result = ""    

for i in range(0, 10):
    myDes = int(input("1~99 사이의 수를 입력하세요 : "))
    
    if myDes == comAnswer:
        result = "정답을 맞췄습니다. 축하합니다 ~"
        print(result)
        exit(0)
    elif myDes > comAnswer:
        result = "더 작은 수입니다"
    elif myDes < comAnswer:
        result = "더 큰 수입니다"
    
    
    print(result)