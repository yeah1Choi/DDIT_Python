import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("pyqt04.ui")[0]

# 클래스 파라미터 값 안에 들어있는건 상속을 받아올 클래스들
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        arr = list(range(1, 45+1))
        
        for i in range(1000):
            rnd = int(random()*45)
            
            temp = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = temp
            
        print(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5])
        
        self.pte1.setPlainText(str(arr[0]))
        self.pte2.setPlainText(str(arr[1]))
        self.pte3.setPlainText(str(arr[2]))
        self.pte4.setPlainText(str(arr[3]))
        self.pte5.setPlainText(str(arr[4]))
        self.pte6.setPlainText(str(arr[5]))
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()