# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SimpleForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 105)
        self.btn_ok = QtWidgets.QToolButton(Form)
        self.btn_ok.setGeometry(QtCore.QRect(250, 30, 81, 41))
        self.btn_ok.setObjectName("btn_ok")
        self.txt_test = QtWidgets.QTextEdit(Form)
        self.txt_test.setGeometry(QtCore.QRect(50, 30, 161, 41))
        self.txt_test.setObjectName("txt_test")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SimpleExample"))
        self.btn_ok.setText(_translate("Form", "Button"))
