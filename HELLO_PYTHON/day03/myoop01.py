class Animal:
    def __init__(self):
        self.full = 1
        print("생성자")
    
    def eat(self, amount):
        self.full += amount
        
    def __del__(self):
        print("소멸자")
        
        
class Human(Animal):
    def __init__(self):
        super().__init__()      
        self.flag_tool = False
        print("생성자")
    
    def momstouch(self):
        self.flag_tool = True
        

if __name__ == "__main__":
    
    ani = Human()
    print("ani.full",ani.full)
    print("hum.flag_tool", ani.flag_tool) 
    
    ani.eat(9)
    ani.momstouch()
    
    print("ani.full",ani.full)
    print("hum.flag_tool", ani.flag_tool)
    
    
    
    