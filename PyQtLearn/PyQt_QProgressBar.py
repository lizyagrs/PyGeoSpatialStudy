from PyQt5.QtWidgets import (QWidget, QProgressBar,QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)#进度条在窗口中的位置，以及宽度和高度
        self.btn = QPushButton('Start', self)#开始按钮
        self.btn.move(40, 80)#按钮在窗口中的位置
        self.btn.clicked.connect(self.doAction)#点击事件

        self.timer = QBasicTimer()#时间条
        self.step = 0 #从0开始记数

        self.setGeometry(300, 300, 280, 170) #弹出窗体在电脑屏幕中的位置，及宽度和高度
        self.setWindowTitle('QProgressBar') #窗体标题
        self.show() #弹出窗体


    def timerEvent(self, e):

        if self.step >= 100: #如果步长到100，则停止
            self.timer.stop()
            self.btn.setText('Finished') #触发按钮的TXT名称，改为完成
            return

        self.step = self.step + 1 # 步长为1，可以修改此参数进行测试
        self.pbar.setValue(self.step) #将步长实时显示到进度条上


    def doAction(self):

        if self.timer.isActive():
            self.timer.stop() #时间显示停止
            self.btn.setText('Start') #设置按钮的名称为开始
        else:
            self.timer.start(100, self) #如果进度条显示的值在100以内
            self.btn.setText('Stop') #设置按钮的名称为停止


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())