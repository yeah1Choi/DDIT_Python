import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("pyqt02.ui")[0]

class MainClass02(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        num = int(self.lbl.text())
        print(num)
        num = 2*num
        print(num)
        self.lbl.setText(str(num))
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass02()
    window.show()
    app.exec_()