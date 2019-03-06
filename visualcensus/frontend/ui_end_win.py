# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_end_win.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 600)
        font = QtGui.QFont()
        font.setPointSize(32)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/wind-smile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_end = QtWidgets.QLabel(self.centralwidget)
        self.label_end.setGeometry(QtCore.QRect(270, 120, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_end.setFont(font)
        self.label_end.setObjectName("label_end")
        self.label_tip = QtWidgets.QLabel(self.centralwidget)
        self.label_tip.setGeometry(QtCore.QRect(280, 350, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_tip.setFont(font)
        self.label_tip.setObjectName("label_tip")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(270, 240, 531, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_result = QtWidgets.QLabel(self.widget)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.horizontalLayout_2.addWidget(self.label_result)
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(170, 15, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_logo.setFont(font)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("Test/images/dekang.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 601, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/dekang.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "测试结束"))
        self.label_end.setText(_translate("MainWindow", "测 试 结 束"))
        self.label_tip.setText(_translate("MainWindow", "请按任意键退出"))
        self.label_2.setText(_translate("MainWindow", "您的视力为："))

