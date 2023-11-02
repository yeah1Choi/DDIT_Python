import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("pyqt06.ui")[0]

# 클래스 파라미터 값 안에 들어있는건 상속을 받아올 클래스들
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        self.pd_reset.clicked.connect(self.btnReset)
        
    def btnClick(self):
        dan = self.sb.value()
        
        for i in range(1, 9+1):
            self.te.append(str(dan)+" X "+str(i)+" = "+str(i*dan))
    
    def btnReset(self):
        self.te.setPlainText("")
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()