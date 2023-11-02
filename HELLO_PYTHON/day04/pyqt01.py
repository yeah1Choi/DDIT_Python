# pyqt를 이용하여 클릭하면 파일을 선택할 수 있는 창을 여는 코드
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("pyqt01.ui")[0]

# 클래스 파라미터 값 안에 들어있는건 상속을 받아올 클래스들
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        print("버튼이 클릭되었습니다.")
        self.lbl.setText("Good Evening")
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()