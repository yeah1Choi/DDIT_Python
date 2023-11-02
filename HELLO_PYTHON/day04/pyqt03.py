import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("pyqt03.ui")[0]

# 클래스 파라미터 값 안에 들어있는건 상속을 받아올 클래스들
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        fn = int(self.te1.toPlainText())
        sn= int(self.te2.toPlainText())
       
        self.te3.setText(str(fn-sn))
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()