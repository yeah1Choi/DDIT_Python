from random import random

def getHolJjak():
    rnd = random()
    
    if rnd > 0.5:
        return "짝"
    else:
        return "홀"
        
com = getHolJjak()
print("com",com)
