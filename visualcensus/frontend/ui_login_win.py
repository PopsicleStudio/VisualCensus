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
        MainWindow.resize(883, 793)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../assets/login_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy)
        self.label_logo.setMinimumSize(QtCore.QSize(0, 48))
        self.label_logo.setBaseSize(QtCore.QSize(0, 1))
        self.label_logo.setAutoFillBackground(False)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../../assets/dekang.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout_3.addWidget(self.label_logo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_welcome = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(46)
        self.label_welcome.setFont(font)
        self.label_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_welcome.setObjectName("label_welcome")
        self.verticalLayout.addWidget(self.label_welcome)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.lineEdit_userName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_userName.setMinimumSize(QtCore.QSize(400, 64))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_userName.setFont(font)
        self.lineEdit_userName.setInputMask("")
        self.lineEdit_userName.setText("")
        self.lineEdit_userName.setFrame(True)
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.horizontalLayout.addWidget(self.lineEdit_userName)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.pushButton_ok = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ok.sizePolicy().hasHeightForWidth())
        self.pushButton_ok.setSizePolicy(sizePolicy)
        self.pushButton_ok.setMinimumSize(QtCore.QSize(144, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_2.addWidget(self.pushButton_ok)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 216, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem9)
        self.label_tip = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_tip.setFont(font)
        self.label_tip.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tip.setObjectName("label_tip")
        self.verticalLayout.addWidget(self.label_tip)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登录"))
        self.label_welcome.setText(_translate("MainWindow", "欢迎使用视力检测系统"))
        self.pushButton_ok.setText(_translate("MainWindow", "OK"))
        self.label_tip.setText(_translate("MainWindow", "请按遥控上的OK键进入测试"))

