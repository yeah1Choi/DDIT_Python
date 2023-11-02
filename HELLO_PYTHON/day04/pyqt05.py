import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("pyqt05.ui")[0]

# 클래스 파라미터 값 안에 들어있는건 상속을 받아올 클래스들
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        self.le_mine.returnPressed.connect(self.btnClick)
        
    def btnClick(self):
        mine = self.le_mine.text();
        
        rnd = random()
        
        com = ""
        if rnd > 0.5:
            com = "짝"
        else:
            com = "홀"
        
        self.le_com.setText(com)
        
        result = ""
        
        if mine == com:
            result = "승리"
        else:
            result = "패배"
            
        self.le_result.setText(result)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()