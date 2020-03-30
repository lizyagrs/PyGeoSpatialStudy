# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,time
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import *
from PyQtLearn.UI.ProgressBar import Ui_Form

#新建ProgressBar类，继承Ui_Form，继承了窗体类，可以继承界面上的所有控件
class ProgressBarForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        #继承Ui_Form
        super(ProgressBarForm, self).__init__()  #初始化父类
        self.setupUi(self)


    def copy_file(self, i):
        self.progressBar.setValue(i)

    def run(self):
        for i in range(101):
            time.sleep(0.1)
            self.progressBar.setValue(i)  # 发送进度条的值 信号

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    #指定弹出窗体
    probarshow=ProgressBarForm()
    probarshow.show()
    sys.exit(app.exec_())