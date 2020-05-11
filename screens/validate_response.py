# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Validate_Response.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from register import Ui_Register_Form


class Ui_MainWindow(object):

    def registerNow(self):
        self.welcomeWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Register_Form()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()        


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 575)
        font = QtGui.QFont()
        font.setFamily("Modern No 20")
        font.setPointSize(-1)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("*{\n"
"font-family:Modern No 20;\n"
"font-size:18px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"background-color:#333;\n"
"border-radius:15px;\n"
"}\n"
"#SignUp_Form{\n"
"background:url(:/newPrefix/Blue.jpg);\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"font-family:Monocorvosia;\n"
"font-size:34px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"\n"
"background-color:red;\n"
"border-radius:14px;\n"
"\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"\n"
"background-color:red;\n"
"border-radius:84px;\n"
"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"font-size:14 px;\n"
"color:white;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:red;\n"
"border-radius:15px;\n"
"background:#49ebff;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"font-size:18px;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid#717072;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 341, 531))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.heading_label = QtWidgets.QLabel(self.frame)
        self.heading_label.setGeometry(QtCore.QRect(100, 0, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Monocorvosia")
        font.setPointSize(-1)
        self.heading_label.setFont(font)
        self.heading_label.setTextFormat(QtCore.Qt.PlainText)
        self.heading_label.setObjectName("heading_label")
        self.Next_btn = QtWidgets.QPushButton(self.frame)
        self.Next_btn.setGeometry(QtCore.QRect(210, 490, 91, 31))
        self.Next_btn.setObjectName("Next_btn")

        self.Next_btn.clicked.connect(self.registerNow)

        self.newmem_label = QtWidgets.QLabel(self.frame)
        self.newmem_label.setGeometry(QtCore.QRect(50, 80, 231, 31))
        self.newmem_label.setObjectName("newmem_label")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(0, 0, 81, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(123, 123))
        self.toolButton.setObjectName("toolButton")
        self.uname_label = QtWidgets.QPlainTextEdit(self.frame)
        self.uname_label.move(10, 120)
        self.uname_label.setObjectName("uname_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.heading_label.setText(_translate("MainWindow", "EXAMINERS"))
        self.Next_btn.setText(_translate("MainWindow", "Next"))
        self.newmem_label.setText(_translate("MainWindow", "--VALIDATION RESULT--"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        message=""
        with open('user_cookie.db', 'r') as file:
            message = file.read()
        self.uname_label.insertPlainText(_translate("MainWindow", message))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
