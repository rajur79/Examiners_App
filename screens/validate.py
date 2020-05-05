# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'validate.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import sqlite3
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from validate_response import Ui_MainWindow


class Ui_SignUp_Form(object):
    def validateNow(self):
        reg_num = self.reg_num.text()
        first_name = '%'+self.first_name.text().upper()+'%'

        connection = sqlite3.connect(".."+os.sep+"database"+os.sep+"login.db")
        result = connection.execute("SELECT examiner_name, designation, council, department, college FROM examiners WHERE reg_no = ? AND upper(examiner_name) like ? order by row_num desc limit 1",(reg_num,first_name))
        data = result.fetchall()
        if(len(data) > 0):
             print("User found")
             f = open("user_cookie.db", "w")
             for row in data:
                examiner_name=row[0].strip()
                designation=row[1].strip()
                council=row[2].strip()
                department=row[3].strip()
                college=row[4].strip()

                f.write("Examiner: "+ examiner_name)
                f.write("\n")
                f.write("Designation: "+ designation)
                f.write("\n")
                f.write("Council: "+ council)
                f.write("\n")
                f.write("Department: "+ department)
                f.write("\n")
                f.write("College: "+ college)
                f.write("\n")
             f.close()
        else:
             print("User not Found") 
             f = open("user_cookie.db", "w")
             f.write("error")
             f.close()

        self.welcomeWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()

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
        self.newmem_label = QtWidgets.QLabel(self.frame)
        self.newmem_label.setGeometry(QtCore.QRect(10, 50, 171, 31))
        self.newmem_label.setObjectName("newmem_label")
        self.reg_num = QtWidgets.QLineEdit(self.frame)
        self.reg_num.setGeometry(QtCore.QRect(60, 100, 231, 20))
        self.reg_num.setObjectName("reg_num")
        self.first_name = QtWidgets.QLineEdit(self.frame)
        self.first_name.setGeometry(QtCore.QRect(60, 150, 231, 20))
        self.first_name.setObjectName("first_name")
        self.toolButton = QtWidgets.QToolButton(SignUp_Form)
        self.toolButton.setGeometry(QtCore.QRect(20, 10, 81, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(123, 123))
        self.toolButton.setObjectName("toolButton")

        self.Next_btn.clicked.connect(self.validateNow)

        self.retranslateUi(SignUp_Form)
        QtCore.QMetaObject.connectSlotsByName(SignUp_Form)

    def retranslateUi(self, SignUp_Form):
        _translate = QtCore.QCoreApplication.translate
        SignUp_Form.setWindowTitle(_translate("SignUp_Form", "Form"))
        self.heading_label.setText(_translate("SignUp_Form", "EXAMINERS"))
        self.Next_btn.setText(_translate("SignUp_Form", "Next"))
        self.newmem_label.setText(_translate("SignUp_Form", "Validate User"))
        self.reg_num.setText(_translate("SignUp_Form", "Registration Number"))
        self.reg_num.setPlaceholderText(_translate("SignUp_Form", "Full Name"))
        self.first_name.setText(_translate("SignUp_Form", "First Name"))
        self.first_name.setPlaceholderText(_translate("SignUp_Form", "Full Name"))
        self.toolButton.setText(_translate("SignUp_Form", "..."))
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
