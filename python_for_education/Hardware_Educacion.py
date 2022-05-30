# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(466, 385)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setGeometry(QtCore.QRect(0, 130, 461, 141))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font: 18pt \"Bell MT\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 275, 351, 31))
        self.pushButton.setStyleSheet("background-color: rgb(201, 226, 101);\n"
"font: 12pt \"Satoshi\";\n"
"border-radius:10px")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        #Button2
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 320, 351, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(242, 242, 242);\n"
"font: 12pt \"Satoshi\";\n"
"border:1px solid rgb(191,191,191);\n"
"border-radius:10px")
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton2")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(QtCore.QRect(170, 0, 141, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./images/Logo_2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowIcon(QIcon("./images/Logo_2.ico"))
        Dialog.setWindowTitle(_translate("Dialog", "Hardware para Educación"))
        self.label_2.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Satoshi\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">¡Hola! Te damos la bienvenida a nuestro Hardware para Educación. Para descargar las librerias orpime el botón de instalar, para conectarte oprime el botón de empezar</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Empezar"))
        self.pushButton_2.setText(_translate("Dialog", "Instalar"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
