'''
类：登录界面
时间： 2019年2月26日15:37:21
'''
from PyQt5.QtWidgets import QMainWindow
from ui_login_win import Ui_MainWindow
import testwindow


class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__()

        self.setupUi(self)
        self.UiConfig()


    def UiConfig(self):

        # 当用户鼠标焦点在输入框且输入信息时，提示信息消失
        self.lineEdit_userName.setPlaceholderText("请输入用户名")
        # 关联切换事件
        self.pushButton_ok.clicked.connect(self.startTest)

        self.show()

    def startTest(self):
        self.hide()
        self.test = testwindow.TestWindow()