class Xi():
    def __init__(self):
        self.cnt_nuclear = 1000
    def dieDev(self, count):
        self.cnt_nuclear += count

class Samsung():
    def __init__(self):
        self.asset = 400   
        self.factory =  20
    def buildFactory(self):
        self.asset -= 4
        self.factory += 1

class Musk():
    def __init__(self):
        self.cnt_sat = 20000
    def shootingRocket(self):
        self.cnt_sat += 100
        
        
class Yewon(Xi,Samsung,Musk):
    def __init__(self):
        Xi.__init__(self)
        Samsung.__init__(self)
        Musk.__init__(self)
        
        
if __name__ == "__main__":
    yw = Yewon()
    
    print(yw.cnt_nuclear)
    print(yw.asset)
    print(yw.factory)
    print(yw.cnt_sat)
    
    yw.dieDev(1000)
    yw.buildFactory()
    yw.shootingRocket()
    print("AFTER")
    
    print(yw.cnt_nuclear)
    print(yw.asset)
    print(yw.factory)
    print(yw.cnt_sat)