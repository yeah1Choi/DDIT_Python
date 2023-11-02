# 첫 별수를 입력하세요 :1
# 끝 별수를 입력하세요 :3

# *
# **
# ***

def getStar(cnt):
    txt = ""
    for i in range(cnt):
        txt += "*"
    return txt

firstNum = int(input("첫 별수를 입력하세요 : "))
lastNum = int(input("끝 별수를 입력하세요 : "))

for i in range(firstNum, lastNum + 1):
    print(getStar(i))