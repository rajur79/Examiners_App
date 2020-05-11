# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3
import os
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register_Form(object):

    row_num=0
    fname=""
    reg_num=""

    def submitCheck(self):
        registrationnumber = self.reg_lineEdit.text()
        firstname = '%'+self.first_name_lineEdit.text().upper()+'%'
        username = self.user_lineEdit.text()
        password = self.pass_lineEdit.text()
        email = self.email_lineEdit.text()        
        mobile = self.mobile_lineEdit.text()

        connection = sqlite3.connect(".."+os.sep+"database"+os.sep+"login.db")

        connection.execute("Insert into login values (?,?,?,?,?,?,?,?)",(registrationnumber, firstname, username, password, email, mobile, datetime.datetime.now(), datetime.datetime.now()))
        connection.commit()

        result = connection.execute("SELECT * FROM LOGIN")
        

        for data in result:
            print("Registration : ", data[0])
            print("FirstName : ", data[1])
            print("Username : ", data[2])
            print("Password : ", data[3])
            print("Email : ", data[4])
            print("Mobile : ", data[5])
            
        connection.close()


    def setupUi(self, Register_Form):
        Register_Form.setObjectName("Register_Form")
        Register_Form.resize(402, 575)
        font = QtGui.QFont()
        font.setFamily("Modern No 20")
        font.setPointSize(-1)
        Register_Form.setFont(font)
        Register_Form.setStyleSheet("*{\n"
"font-family:Modern No 20;\n"
"font-size:18px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"background-color:#333;\n"
"border-radius:15px;\n"
"}\n"
"#Register_Form{\n"
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
"border-radius:54px;\n"
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
        self.frame = QtWidgets.QFrame(Register_Form)
        self.frame.setGeometry(QtCore.QRect(20, 60, 351, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.heading_label = QtWidgets.QLabel(self.frame)
        self.heading_label.setGeometry(QtCore.QRect(110, 60, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Monocorvosia")
        font.setPointSize(-1)
        self.heading_label.setFont(font)
        self.heading_label.setTextFormat(QtCore.Qt.PlainText)
        self.heading_label.setObjectName("heading_label")
        self.submit_btn = QtWidgets.QPushButton(self.frame)
        self.submit_btn.setGeometry(QtCore.QRect(230, 430, 91, 31))
        self.submit_btn.setObjectName("submit_btn")

        self.submit_btn.clicked.connect(self.submitCheck)
        
        self.newmem_label = QtWidgets.QLabel(self.frame)
        self.newmem_label.setGeometry(QtCore.QRect(20, 100, 171, 31))
        self.newmem_label.setObjectName("newmem_label")

        self.regnum_label = QtWidgets.QLabel(self.frame)
        self.regnum_label.setGeometry(QtCore.QRect(60, 180, 231, 20))
        self.regnum_label.setObjectName("regnum_label")

        self.fname_label = QtWidgets.QLabel(self.frame)
        self.fname_label.setGeometry(QtCore.QRect(60, 220, 231, 20))
        self.fname_label.setObjectName("fname_label")

        self.email_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.email_lineEdit.setGeometry(QtCore.QRect(60, 260, 231, 20))
        self.email_lineEdit.setText("")
        self.email_lineEdit.setObjectName("email_lineEdit")

        self.pass_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.pass_lineEdit.setGeometry(QtCore.QRect(60, 300, 231, 20))
        self.pass_lineEdit.setText("")
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit.setObjectName("pass_lineEdit")
                
        self.mobile_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.mobile_lineEdit.setGeometry(QtCore.QRect(60, 340, 231, 20))
        self.mobile_lineEdit.setText("")
        self.mobile_lineEdit.setObjectName("mobile_lineEdit")
        
        self.toolButton = QtWidgets.QToolButton(Register_Form)
        self.toolButton.setGeometry(QtCore.QRect(130, 10, 121, 111))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(123, 123))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Register_Form)
        QtCore.QMetaObject.connectSlotsByName(Register_Form)

    def retranslateUi(self, Register_Form):

        f = open('user_cookie.db', 'r')
        for line in f:
            if line.startswith("ID:"):
                Ui_Register_Form.row_num=line.split("ID: ")[1]
                print("row_num:" +Ui_Register_Form.row_num)
            elif line.startswith("Examiner:"):
                Ui_Register_Form.fname=line.split("Examiner: ")[1]
                print("fname: "+Ui_Register_Form.fname)
            elif line.startswith("Reg Num:"):
                Ui_Register_Form.reg_num=line.split("Reg Num: ")[1]

        _translate = QtCore.QCoreApplication.translate
        Register_Form.setWindowTitle(_translate("Register_Form", "Form"))
        self.heading_label.setText(_translate("Register_Form", "EXAMINERS"))
        self.newmem_label.setText(_translate("Register_Form", "Registration"))
        self.regnum_label.setText(_translate("Register_Form", "Reg Num : " +Ui_Register_Form.reg_num))
        self.fname_label.setText(_translate("Register_Form", "Name: " +Ui_Register_Form.fname))
        self.email_lineEdit.setPlaceholderText(_translate("Register_Form", "Email"))
        self.pass_lineEdit.setPlaceholderText(_translate("Register_Form", "Password"))
        self.mobile_lineEdit.setPlaceholderText(_translate("Register_Form", "Mobile Number"))
        self.submit_btn.setText(_translate("Register_Form", "Submit"))
        self.toolButton.setText(_translate("Register_Form", "..."))
       

        
import blue_rc
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register_Form = QtWidgets.QWidget()
    ui = Ui_Register_Form()
    ui.setupUi(Register_Form)
    Register_Form.show()
    sys.exit(app.exec_())
