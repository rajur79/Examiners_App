# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Welcome_Form(object):
    def setupUi(self, Welcome_Form):
        Welcome_Form.setObjectName("Welcome_Form")
        Welcome_Form.resize(371, 550)
        font = QtGui.QFont()
        font.setFamily("Modern No 20")
        font.setPointSize(-1)
        Welcome_Form.setFont(font)
        Welcome_Form.setStyleSheet("*{\n"
"font-family:Modern No 20;\n"
"font-size:18px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"background-color:#333;\n"
"border-radius:15px;\n"
"}\n"
"#Welcome_Form{\n"
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
        self.frame = QtWidgets.QFrame(Welcome_Form)
        self.frame.setGeometry(QtCore.QRect(20, 30, 311, 471))
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
        self.logout_btn = QtWidgets.QPushButton(self.frame)
        self.logout_btn.setGeometry(QtCore.QRect(220, 30, 81, 31))
        self.logout_btn.setObjectName("logout_btn")
        self.welc_label = QtWidgets.QLabel(self.frame)
        self.welc_label.setGeometry(QtCore.QRect(10, 50, 171, 31))
        self.welc_label.setObjectName("welc_label")
        self.renum_btn = QtWidgets.QPushButton(self.frame)
        self.renum_btn.setGeometry(QtCore.QRect(30, 310, 251, 31))
        self.renum_btn.setObjectName("renum_btn")
        self.ugexam_btn = QtWidgets.QPushButton(self.frame)
        self.ugexam_btn.setGeometry(QtCore.QRect(30, 170, 251, 31))
        self.ugexam_btn.setObjectName("ugexam_btn")
        self.pgexam_btn = QtWidgets.QPushButton(self.frame)
        self.pgexam_btn.setGeometry(QtCore.QRect(30, 240, 251, 31))
        self.pgexam_btn.setObjectName("pgexam_btn")
        self.toolButton = QtWidgets.QToolButton(Welcome_Form)
        self.toolButton.setGeometry(QtCore.QRect(20, 10, 81, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(123, 123))
        self.toolButton.setObjectName("toolButton")

        self.uname_label = QtWidgets.QPlainTextEdit(self.frame)
        self.uname_label.move(50, 100)
        self.uname_label.setObjectName("uname_label")
        self.uname_label.setGeometry(QtCore.QRect(29, 100, 282, 62))

        self.retranslateUi(Welcome_Form)
        QtCore.QMetaObject.connectSlotsByName(Welcome_Form)

    def retranslateUi(self, Welcome_Form):
        _translate = QtCore.QCoreApplication.translate
        Welcome_Form.setWindowTitle(_translate("Welcome_Form", "Form"))
        self.heading_label.setText(_translate("Welcome_Form", "EXAMINERS"))
        self.logout_btn.setText(_translate("Welcome_Form", "Log Out"))
        self.welc_label.setText(_translate("Welcome_Form", "WELCOME :"))
        self.renum_btn.setText(_translate("Welcome_Form", "Renumeration"))
        self.ugexam_btn.setText(_translate("Welcome_Form", "Undergraduate Examiners"))
        self.pgexam_btn.setText(_translate("Welcome_Form", "Postgraduate Examiners"))
        self.toolButton.setText(_translate("Welcome_Form", "..."))
        message=""
        with open('user_cookie.db', 'r') as file:
            line = file.readline()
            while line:
                if line.startswith('Examiner'):
                    self.uname_label.insertPlainText(_translate("MainWindow", line))
                elif line.startswith('ID: '):
                    Ui_Welcome_Form.row_num = line.split("ID: ")[1]
                line = file.readline()
                
import blue_rc
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Welcome_Form = QtWidgets.QWidget()
    ui = Ui_Welcome_Form()
    ui.setupUi(Welcome_Form)
    Welcome_Form.show()
    sys.exit(app.exec_())
