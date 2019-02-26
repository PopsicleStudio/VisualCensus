'''
说明： 主界面 三个界面之间的切换
时间： 2019年2月26日15:43:28
'''
from PyQt5.QtWidgets import (QMainWindow, QWidget)

from loginwindow import LoginWindow
from endwindow import EndWindow


class MainWindow(QMainWindow, QWidget):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.EnterLogin()

    def EnterLogin(self):
        self.Login =LoginWindow(self)

    def endTest(self):
        self.End = EndWindow()
        self.show()

