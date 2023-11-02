myresult = 0

def showDan(dan):
    
    for i in range(1, 9+1):
        print(str(dan)+"*"+str(i)+"="+str(i*dan))
    
showDan(5)