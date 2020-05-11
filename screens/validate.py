# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'validate.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from validate_response import Ui_MainWindow


class Ui_Validate_Form(object):

    def validateNow(self):
        council = self.council_comboBox.currentText()
        reg_num = self.reg_num.text()
        first_name = '%'+self.first_name.text().upper()+'%'

        connection = sqlite3.connect(".."+os.sep+"database"+os.sep+"login.db")
        result = connection.execute("SELECT row_num, examiner_name, designation, council, department, college FROM examiners WHERE reg_no = ? AND upper(examiner_name) like ? AND council = ? order by row_num desc limit 1",(reg_num,first_name,council))
        data = result.fetchall()
        if(len(data) > 0):
            print("User found")
            f = open("user_cookie.db", "w")
            for row in data:
                row_num=row[0]
                examiner_name=row[1].strip()
                designation=row[2].strip()
                council=row[3].strip()
                department=row[4].strip()
                college=row[5].strip()

                f.write("ID: "+ str(row_num))
                f.write("\n")
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
    
    def setupUi(self, Validate_Form):
        Validate_Form.setObjectName("Validate_Form")
        Validate_Form.resize(402, 575)
        font = QtGui.QFont()
        font.setFamily("Modern No 20")
        font.setPointSize(-1)
        Validate_Form.setFont(font)
        Validate_Form.setStyleSheet("*{\n"
"font-family:Modern No 20;\n"
"font-size:18px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"background-color:#333;\n"
"border-radius:15px;\n"
"}\n"
"#Validate_Form{\n"
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
        self.frame = QtWidgets.QFrame(Validate_Form)
        self.frame.setGeometry(QtCore.QRect(30, 120, 341, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.heading_label = QtWidgets.QLabel(self.frame)
        self.heading_label.setGeometry(QtCore.QRect(100, 110, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Monocorvosia")
        font.setPointSize(-1)
        self.heading_label.setFont(font)
        self.heading_label.setTextFormat(QtCore.Qt.PlainText)
        self.heading_label.setObjectName("heading_label")
        self.enter_btn = QtWidgets.QPushButton(self.frame)
        self.enter_btn.setGeometry(QtCore.QRect(180, 330, 91, 31))
        self.enter_btn.setObjectName("enter_btn")
        self.newmem_label = QtWidgets.QLabel(self.frame)
        self.newmem_label.setGeometry(QtCore.QRect(30, 150, 171, 31))
        self.newmem_label.setObjectName("newmem_label")
        self.reg_num = QtWidgets.QLineEdit(self.frame)
        self.reg_num.setGeometry(QtCore.QRect(60, 240, 231, 20))
        self.reg_num.setText("")
        self.reg_num.setObjectName("reg_num")
        self.first_name = QtWidgets.QLineEdit(self.frame)
        self.first_name.setGeometry(QtCore.QRect(60, 290, 231, 20))
        self.first_name.setText("")
        self.first_name.setObjectName("first_name")
        self.council_comboBox = QtWidgets.QComboBox(self.frame)
        self.council_comboBox.setGeometry(QtCore.QRect(60, 190, 231, 31))
        self.council_comboBox.setObjectName("council_comboBox")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.council_comboBox.addItem("")
        self.toolButton = QtWidgets.QToolButton(Validate_Form)
        self.toolButton.setGeometry(QtCore.QRect(110, 30, 181, 181))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(123, 123))
        self.toolButton.setObjectName("toolButton")

        self.enter_btn.clicked.connect(self.validateNow)

        self.retranslateUi(Validate_Form)
        QtCore.QMetaObject.connectSlotsByName(Validate_Form)

    def retranslateUi(self, Validate_Form):
        _translate = QtCore.QCoreApplication.translate
        Validate_Form.setWindowTitle(_translate("Validate_Form", "Form"))
        self.heading_label.setText(_translate("Validate_Form", "EXAMINERS"))
        self.enter_btn.setText(_translate("Validate_Form", "Enter"))
        self.newmem_label.setText(_translate("Validate_Form", "Validate User"))
        self.reg_num.setPlaceholderText(_translate("Validate_Form", "Registration Number"))
        self.first_name.setPlaceholderText(_translate("Validate_Form", "First Name"))
        self.council_comboBox.setItemText(0, _translate("Validate_Form", "Medical Council"))
        self.council_comboBox.setItemText(1, _translate("Validate_Form", "Andhra Pradesh Medical Council"))
        self.council_comboBox.setItemText(2, _translate("Validate_Form", "Arunachal Pradesh Medical Council"))
        self.council_comboBox.setItemText(3, _translate("Validate_Form", "Assam Medical Council"))
        self.council_comboBox.setItemText(4, _translate("Validate_Form", "Bareilly Medical Council"))
        self.council_comboBox.setItemText(5, _translate("Validate_Form", "Bihar Medical Council"))
        self.council_comboBox.setItemText(6, _translate("Validate_Form", "Bombay Medical Council"))
        self.council_comboBox.setItemText(7, _translate("Validate_Form", "Chandigarh Medical Council"))
        self.council_comboBox.setItemText(8, _translate("Validate_Form", "Chattisgarh Medical Council"))
        self.council_comboBox.setItemText(9, _translate("Validate_Form", "Delhi Medical Council"))
        self.council_comboBox.setItemText(10, _translate("Validate_Form", "Dental Council of India"))
        self.council_comboBox.setItemText(11, _translate("Validate_Form", "Goa Medical Council"))
        self.council_comboBox.setItemText(12, _translate("Validate_Form", "Gujarat Medical Council"))
        self.council_comboBox.setItemText(13, _translate("Validate_Form", "Haryana Medical Council"))
        self.council_comboBox.setItemText(14, _translate("Validate_Form", "Himanchal Pradesh Medical Council"))
        self.council_comboBox.setItemText(15, _translate("Validate_Form", "Hyderabad Medical Council"))
        self.council_comboBox.setItemText(16, _translate("Validate_Form", "Jammu & Kashmir Medical Council"))
        self.council_comboBox.setItemText(17, _translate("Validate_Form", "Karnataka Medical Council"))
        self.council_comboBox.setItemText(18, _translate("Validate_Form", "Kerala Medical Council"))
        self.council_comboBox.setItemText(19, _translate("Validate_Form", "Madhya Pradesh Medical Council"))
        self.council_comboBox.setItemText(20, _translate("Validate_Form", "Madras Medical Council"))
        self.council_comboBox.setItemText(21, _translate("Validate_Form", "Mahakoshal Medical Council"))
        self.council_comboBox.setItemText(22, _translate("Validate_Form", "Manipur Medical Council"))
        self.council_comboBox.setItemText(23, _translate("Validate_Form", "Medical Council of India"))
        self.council_comboBox.setItemText(24, _translate("Validate_Form", "Mizoram Medical Council"))
        self.council_comboBox.setItemText(25, _translate("Validate_Form", "Mysore Medical Council"))
        self.council_comboBox.setItemText(26, _translate("Validate_Form", "Nagaland Medical Council"))
        self.council_comboBox.setItemText(27, _translate("Validate_Form", "Nepal Medical Council"))
        self.council_comboBox.setItemText(28, _translate("Validate_Form", "Orissa Council of Medical Registration"))
        self.council_comboBox.setItemText(29, _translate("Validate_Form", "Others"))
        self.council_comboBox.setItemText(30, _translate("Validate_Form", "Pondicherry Medical Council"))
        self.council_comboBox.setItemText(31, _translate("Validate_Form", "Punjab Medical Council"))
        self.council_comboBox.setItemText(32, _translate("Validate_Form", "Rajasthan Medical Council"))
        self.council_comboBox.setItemText(33, _translate("Validate_Form", "Sikkim Medical Council"))
        self.council_comboBox.setItemText(34, _translate("Validate_Form", "Tamil Nadu Medical Council"))
        self.council_comboBox.setItemText(35, _translate("Validate_Form", "Telangana State Medical Council"))
        self.council_comboBox.setItemText(36, _translate("Validate_Form", "Travancore Cochin Medical Council"))
        self.council_comboBox.setItemText(37, _translate("Validate_Form", "Travancore Cochin Medical Council, Trivandrum"))
        self.council_comboBox.setItemText(38, _translate("Validate_Form", "Tripura State Medical Council"))
        self.council_comboBox.setItemText(39, _translate("Validate_Form", "Uttar Pradesh Medical Council"))
        self.council_comboBox.setItemText(40, _translate("Validate_Form", "Uttarakhand Medical Council"))
        self.council_comboBox.setItemText(41, _translate("Validate_Form", "Vidharba Medical Council"))
        self.council_comboBox.setItemText(42, _translate("Validate_Form", "West Bengal Medical Council"))
        self.toolButton.setText(_translate("Validate_Form", "..."))
import blue_rc
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Validate_Form = QtWidgets.QWidget()
    ui = Ui_Validate_Form()
    ui.setupUi(Validate_Form)
    Validate_Form.show()
    sys.exit(app.exec_())
