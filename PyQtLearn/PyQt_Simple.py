# -*- coding: utf-8 -*-
import sys
#基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import (QWidget, QToolTip,QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        #当需要继承父类构造函数中的内容，且子类需要在父类的基础上补充时，使用super().__init__()方法
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('这是一个按钮')
        btn = QPushButton('按钮', self)
        btn.setToolTip('这是一个按钮')
        btn.resize(btn.sizeHint())
        btn.move(100, 100)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())