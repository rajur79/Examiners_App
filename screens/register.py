# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import sqlite3
import os
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUp_Form(object):

    row_num=0

    def registerNow(self):
        email = self.email.text()
        password = self.password.text()
        mobile = self.mobile.text()

        print(email + ":" +password+ ":" +mobile+ ":" +Ui_SignUp_Form.row_num)
        connection = sqlite3.connect(".."+os.sep+"database"+os.sep+"login.db")

        connection.execute("Insert into login values (?,?,?,?,?,?)",(Ui_SignUp_Form.row_num, email, password, mobile, datetime.datetime.now(), datetime.datetime.now()))
        connection.commit()
        connection.close()

    def setupUi(self, SignUp_Form):
        SignUp_Form.setObjectName("SignUp_Form")
        SignUp_Form.resize(402, 575)
        font = QtGui.QFont()
        font.setFamily("Modern No 20")
        font.setPointSize(-1)
        SignUp_Form.setFont(font)
        SignUp_Form.setStyleSheet("*{\n"
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
"}\n"
"")
        self.frame = QtWidgets.QFrame(SignUp_Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 341, 531))
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
        self.newmem_label.setGeometry(QtCore.QRect(10, 50, 171, 31))
        self.newmem_label.setObjectName("newmem_label")
        self.email = QtWidgets.QLineEdit(self.frame)
        self.email.setGeometry(QtCore.QRect(60, 100, 231, 20))
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(60, 150, 231, 20))
        self.password.setObjectName("password")
        self.mobile = QtWidgets.QLineEdit(self.frame)
        self.mobile.setGeometry(QtCore.QRect(60, 200, 231, 20))
        self.mobile.setObjectName("mobile")
        self.toolButton = QtWidgets.QToolButton(SignUp_Form)
        self.toolButton.setGeometry(QtCore.QRect(20, 10, 81, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(123, 123))
        self.toolButton.setObjectName("toolButton")

        self.uname_label = QtWidgets.QPlainTextEdit(self.frame)
        self.uname_label.move(30, 280)
        self.uname_label.setObjectName("uname_label")

        self.retranslateUi(SignUp_Form)
        QtCore.QMetaObject.connectSlotsByName(SignUp_Form)

    def retranslateUi(self, SignUp_Form):
        _translate = QtCore.QCoreApplication.translate
        SignUp_Form.setWindowTitle(_translate("SignUp_Form", "Form"))
        self.heading_label.setText(_translate("SignUp_Form", "EXAMINERS"))
        self.Next_btn.setText(_translate("SignUp_Form", "Next"))
        self.newmem_label.setText(_translate("SignUp_Form", "Registration"))
        self.email.setText(_translate("SignUp_Form", "Email"))
        self.email.setPlaceholderText(_translate("SignUp_Form", "Full Name"))
        self.password.setText(_translate("SignUp_Form", "Password"))
        self.password.setPlaceholderText(_translate("SignUp_Form", "Full Name"))
        self.mobile.setText(_translate("SignUp_Form", "Mobile Number"))
        self.mobile.setPlaceholderText(_translate("SignUp_Form", "Full Name"))
        self.toolButton.setText(_translate("SignUp_Form", "..."))
        message=""
        with open('user_cookie.db', 'r') as file:
            line = file.readline()
            while line:
                if line.startswith('Examiner'):
                    self.uname_label.insertPlainText(_translate("MainWindow", line))
                elif line.startswith('ID: '):
                    Ui_SignUp_Form.row_num = line.split("ID: ")[1]
                line = file.readline()

import blue_rc
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUp_Form = QtWidgets.QWidget()
    ui = Ui_SignUp_Form()
    ui.setupUi(SignUp_Form)
    SignUp_Form.show()
    sys.exit(app.exec_())
