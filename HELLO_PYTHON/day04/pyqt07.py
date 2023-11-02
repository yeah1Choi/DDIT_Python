import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("pyqt07.ui")[0]

# 클래스 파라미터 값 안에 들어있는건 상속을 받아올 클래스들
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        self.le_mine.returnPressed.connect(self.btnClick)
        
    def btnClick(self):
        mine = self.le_mine.text()
        
        com = ""
        
        rnd = random()
        if rnd < 0.33:
            com = "가위"
        elif rnd < 0.66:
            com = "바위"
        else:
            com = "보"
        
        self.le_com.setText(com)
            
        result = ""
        
        if mine == com :
            result = "비겼습니다"
            
        elif mine == "가위" and com == "보":
            result = "이겼습니다" 
        elif mine == "바위" and com == "가위":
            result = "이겼습니다" 
        elif mine == "보" and com == "바위":
            result = "이겼습니다"  
             
        else :
            result = "졌습니다"
            
        self.le_result.setText(result)    
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()