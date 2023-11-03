# pyqt를 이용하여 클릭하면 파일을 선택할 수 있는 창을 여는 코드
import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton

form_class = uic.loadUiType("myOmok02.ui")[0]

# 클래스 파라미터 값 안에 들어있는건 상속을 받아올 클래스들
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.flag = True
        self.setupUi(self)
        
        for i in range(10):
            for j in range(10):
                pb = QPushButton("", self)
                pb.setIcon(QtGui.QIcon('images/0.png')) 
                pb.setIconSize(QtCore.QSize(40,40))
                pb.setGeometry(QtCore.QRect(i*40, j*40, 40, 40))
                pb.clicked.connect(self.myclick)
                
        self.resize(400, 400)
        self.show()  
        
       
    def myclick(self):
        
        if self.flag:
            self.sender().setIcon(QtGui.QIcon('images/1.png')) 
        else:
            self.sender().setIcon(QtGui.QIcon('images/2.png'))
         
        self.flag = not self.flag
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()