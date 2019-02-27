'''
说明： 主界面 三个界面之间的切换
时间： 2019年2月26日15:43:28
'''
from PyQt5.QtWidgets import (QMainWindow, QWidget)

from loginwindow import LoginWindow
from testwindow import TestWindow
from endwindow import EndWindow


class MainWindow(QMainWindow, QWidget):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.EnterLogin()

    def EnterLogin(self):
        self.Ui_Login =LoginWindow(self)
        # 关联切换事件
        self.Ui_Login.pushButton_ok.clicked.connect(self.startTest)

    def startTest(self):
        self.Ui_Login.hide()
        self.Ui_Test = TestWindow()
        self.Ui_Test.test_end_event.connect(self.testResult)

    def testResult(self):
        self.Ui_Test.hide()
        self.Ui_End = EndWindow(self.Ui_Test.vision_value)
        self.Ui_End.return_login_event.connect(self.returnLogin)

    def returnLogin(self):
        self.Ui_End.hide()
        self.EnterLogin()


