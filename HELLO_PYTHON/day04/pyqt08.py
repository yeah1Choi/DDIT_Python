import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("pyqt08.ui")[0]

# 클래스 파라미터 값 안에 들어있는건 상속을 받아올 클래스들
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        self.sbLast.valueChanged.connect(self.btnClick)
        
    def getStar(self):
        txt = ""
        for i in range(self):
            txt += "*"
        return txt        
    
    def btnClick(self):
        first = self.sbFirst.value()
        last = self.sbLast.value()
        
        txt = ""
        
        for i in range(first, last + 1):
            txt += self.getStar(i) + "\n"
        
        self.pte.setPlainText(txt)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()