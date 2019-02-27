# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login_win.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 669)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/login_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-image: url(:/new/prefix1/back.jpg);\n"
"}\n"
" \n"
"QLineEdit{\n"
" \n"
"    border:2px solid#7b7b7b;\n"
"    border-radius:12px;\n"
"    background-color:#fffef0\n"
"}\n"
" \n"
"QPushButton{\n"
"    border:2px solid#7b7b7b;\n"
"    border-radius:24px;\n"
"    background-color:#6a92ff;\n"
"    font: 75 26pt \"Arial\";\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color:#aa92ff\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#FF90ff\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_welcome = QtWidgets.QLabel(self.centralwidget)
        self.label_welcome.setGeometry(QtCore.QRect(140, 120, 621, 71))
        font = QtGui.QFont()
        font.setPointSize(46)
        self.label_welcome.setFont(font)
        self.label_welcome.setObjectName("label_welcome")
        self.lineEdit_userName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_userName.setGeometry(QtCore.QRect(210, 260, 471, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_userName.setFont(font)
        self.lineEdit_userName.setInputMask("")
        self.lineEdit_userName.setText("")
        self.lineEdit_userName.setFrame(True)
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(160, 30, 541, 51))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("tests/images/dekang.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.label_tip = QtWidgets.QLabel(self.centralwidget)
        self.label_tip.setGeometry(QtCore.QRect(260, 480, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_tip.setFont(font)
        self.label_tip.setObjectName("label_tip")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 611, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/dekang.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_ok = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ok.setGeometry(QtCore.QRect(360, 400, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setObjectName("pushButton_ok")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_welcome.setText(_translate("MainWindow", "欢迎使用视力检测系统"))
        self.label_tip.setText(_translate("MainWindow", "请按遥控上的OK键进入测试"))
        self.pushButton_ok.setText(_translate("MainWindow", "OK"))

