import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from PyQtLearn.UI.SimpleForm import Ui_Form

class SimpleForm(QtWidgets.QWidget,Ui_Form):

    def __init__(self):
        #继承Ui_Form
        super(SimpleForm, self).__init__()  #初始化父类
        self.setupUi(self)

        self.btn_ok.clicked.connect(self.btn_ok_click)

    def btn_ok_click(self):
        print('ok')
        text = self.txt_test.toPlainText()
        print("text:",text)
        msg_box = QMessageBox(QMessageBox.Warning, "Alert", text)
        msg_box.exec_()



if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    #指定弹出窗体
    Smshow=SimpleForm()
    Smshow.show()
    sys.exit(app.exec_())