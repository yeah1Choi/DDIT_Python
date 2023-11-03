# pyqt를 이용하여 클릭하면 파일을 선택할 수 있는 창을 여는 코드
import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton

form_class = uic.loadUiType("myOmok03.ui")[0]

# 클래스 파라미터 값 안에 들어있는건 상속을 받아올 클래스들
class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.flag = True
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
                        
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
        self.pb2D = []
        self.setupUi(self)
        
        for i in range(10):
            line = []
            for j in range(10):
                pb = QPushButton("", self)
                pb.setToolTip("{},{}".format(i,j))
                pb.setIcon(QtGui.QIcon('images/0.png')) 
                pb.setIconSize(QtCore.QSize(40,40))
                pb.setGeometry(QtCore.QRect(j*40, i*40, 40, 40))
                pb.clicked.connect(self.myclick)
                line.append(pb)
            self.pb2D.append(line)
            
                
        self.show()  
        self.myrender();
    
    # 렌더링 함수 : 배열의 값을 가져가 화면에 출력하게 만드는 함수
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('images/0.png'))
                
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('images/1.png'))
                
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('images/2.png'))
    
    # 방향에 따라 돌의 갯수를 세는 함수들 ~
    def getUp(self, i, j, stone):
        cnt = 0
        # 배열은 9까지인데 10으로 넘어감으로 try-except로 예외처리함
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else: 
                    return cnt
        except:
            return cnt
            
    def getDW(self, i, j, stone):
        cnt = 0

        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else: 
                    return cnt
        except:
            return cnt
    
    
    # QPushButton 버튼 클릭 이벤트 함수                
    def myclick(self):
        strij = self.sender().toolTip()
        strijArr = strij.split(',')
        
        i = int(strijArr[0])
        j = int(strijArr[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = -1
        
        if self.flag:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
            
        up = self.getUp(i,j,stone)
        dw = self.getDW(i,j,stone)
        
        print("up",up)
        print("dw",dw)
        
        self.myrender()
         
        self.flag = not self.flag
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()