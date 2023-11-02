# 가위/바위/보를 선택하세요 :가위
# 나 :가위
# 컴 :바위   * ~0.3:가위, ~0.6:바위, 나머지:보
# 결과 :패배
from random import random

myDes = input("가위/바위/보를 선택하세요 : ");

comDes = ""
rnd = random()
if rnd < 0.33:
    comDes = "가위"
elif rnd < 0.66:
    comDes = "바위"
else:
    comDes = "보"
    
result = ""

if myDes == comDes :
    result = "비겼습니다"
    
elif myDes == "가위" and comDes == "보":
    result = "이겼습니다" 
elif myDes == "바위" and comDes == "가위":
    result = "이겼습니다" 
elif myDes == "보" and comDes == "바위":
    result = "이겼습니다"  
     
else :
    result = "졌습니다"
    
print("당신은 {}, 컴퓨터는 {} => 당신은 {}.".format(myDes, comDes, result))
