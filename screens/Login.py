# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from validate import Ui_Validate_Form
import os
from register import Ui_Register_Form
import sqlite3



class Ui_Login_Form(object):
    def SignInCheck(self):
        username = self.user_lineEdit.text()
        password = self.pass_lineEdit.text()

        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM LOGIN WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        if (len(result.fetchall()) > 0):
            print("User Found !")
        else:
            print("User Not Found !")
        
            
    def SignUpCheck(self):
        print(" signup button clicked")
        
    def setupUi(self, Login_Form):
        Login_Form.setObjectName("Login_Form")
        Login_Form.resize(403, 536)
        font = QtGui.QFont()
        font.setFamily("Modern No 20")
        font.setPointSize(-1)
        Login_Form.setFont(font)
        Login_Form.setStyleSheet("*{\n"
"font-family:Modern No 20;\n"
"font-size:18px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"background-color:#333;\n"
"border-radius:15px;\n"
"}\n"
"#Login_Form{\n"
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
"border-radius:64px;\n"
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
        self.frame = QtWidgets.QFrame(Login_Form)
        self.frame.setGeometry(QtCore.QRect(60, 90, 301, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.heading_label = QtWidgets.QLabel(self.frame)
        self.heading_label.setGeometry(QtCore.QRect(50, 90, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Monocorvosia")
        font.setPointSize(-1)
        self.heading_label.setFont(font)
        self.heading_label.setTextFormat(QtCore.Qt.PlainText)
        self.heading_label.setObjectName("heading_label")
        self.SignUp_btn = QtWidgets.QPushButton(self.frame)
        self.SignUp_btn.setGeometry(QtCore.QRect(20, 340, 261, 31))
        self.SignUp_btn.setObjectName("SignUp_btn")
        #############################Button Event############################
        self.SignUp_btn.clicked.connect(self.SignUpCheck)
        #################################################################
        self.SignIn_btn = QtWidgets.QPushButton(self.frame)
        self.SignIn_btn.setGeometry(QtCore.QRect(20, 250, 261, 31))
        self.SignIn_btn.setObjectName("SignIn_btn")
        #############################Button Event############################
        self.SignIn_btn.clicked.connect(self.SignInCheck)
        #################################################################
        self.exist_label = QtWidgets.QLabel(self.frame)
        self.exist_label.setGeometry(QtCore.QRect(20, 130, 171, 31))
        self.exist_label.setObjectName("exist_label")
        self.newm_label = QtWidgets.QLabel(self.frame)
        self.newm_label.setGeometry(QtCore.QRect(20, 300, 271, 31))
        self.newm_label.setObjectName("newm_label")
        self.user_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.user_lineEdit.setGeometry(QtCore.QRect(40, 170, 231, 20))
        self.user_lineEdit.setText("")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.pass_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.pass_lineEdit.setGeometry(QtCore.QRect(40, 210, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Modern No 20")
        font.setPointSize(-1)
        self.pass_lineEdit.setFont(font)
        self.pass_lineEdit.setText("")
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.toolButton = QtWidgets.QToolButton(Login_Form)
        self.toolButton.setGeometry(QtCore.QRect(120, 10, 181, 181))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(123, 123))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Login_Form)
        QtCore.QMetaObject.connectSlotsByName(Login_Form)

    def retranslateUi(self, Login_Form):
        _translate = QtCore.QCoreApplication.translate
        Login_Form.setWindowTitle(_translate("Login_Form", "Form"))
        self.heading_label.setText(_translate("Login_Form", "EXAMINERS"))
        self.SignUp_btn.setText(_translate("Login_Form", "Sign Up"))
        self.SignIn_btn.setText(_translate("Login_Form", "Sign In"))
        self.exist_label.setText(_translate("Login_Form", "Existing Member !"))
        self.newm_label.setText(_translate("Login_Form", "New Member !"))
        self.user_lineEdit.setPlaceholderText(_translate("Login_Form", "Username"))
        self.pass_lineEdit.setPlaceholderText(_translate("Login_Form", "Password"))
        self.toolButton.setText(_translate("Login_Form", "..."))
import blue_rc
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Form = QtWidgets.QWidget()
    ui = Ui_Login_Form()
    ui.setupUi(Login_Form)
    Login_Form.show()
    sys.exit(app.exec_())
