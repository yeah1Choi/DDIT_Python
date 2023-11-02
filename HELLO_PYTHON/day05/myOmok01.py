# pyqt를 이용하여 클릭하면 파일을 선택할 수 있는 창을 여는 코드
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton

form_class = uic.loadUiType("myOmok01.ui")[0]

# 클래스 파라미터 값 안에 들어있는건 상속을 받아올 클래스들
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.initUI()
        
    def initUI(self):
        for i in range(0, 9+1):
            for j in range(0, 9+1):
                btn = QPushButton("", self)
                btn.resize(40,40)
                btn.move(40*i, 40*j)
                btn.setStyleSheet('border-image:url(./images/0.png);border:0px;')
        
        self.resize(400, 400)
        self.show()   
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()