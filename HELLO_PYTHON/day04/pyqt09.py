import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from random import random

form_class = uic.loadUiType("pyqt09.ui")[0]

# 클래스 파라미터 값 안에 들어있는건 상속을 받아올 클래스들
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb01.clicked.connect(self.btnNum)
        self.pb02.clicked.connect(self.btnNum)
        self.pb03.clicked.connect(self.btnNum)
        self.pb04.clicked.connect(self.btnNum)
        self.pb05.clicked.connect(self.btnNum)
        self.pb06.clicked.connect(self.btnNum)
        self.pb07.clicked.connect(self.btnNum)
        self.pb08.clicked.connect(self.btnNum)
        self.pb09.clicked.connect(self.btnNum)
        self.pb00.clicked.connect(self.btnNum)
        
        self.pbCall.clicked.connect(self.btnCall)
        
    def btnNum(self):
        # self.sender() : 클릭된 버튼의 객체를 가져오는 PyQt의 메소드
        # 객체만 가져왔으니 기존의 꺼내는 방식을 알아서 꺼내가면된다
        new_txt = self.sender().text()
        
        current_txt = self.le.text()
        self.le.setText(current_txt + new_txt)
    
    def btnCall(self):       
        tel = self.le.text()
        QMessageBox.about(self, "message", "calling to "+tel)
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()