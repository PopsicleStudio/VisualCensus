"""
类：登录界面
时间： 2019年2月26日15:37:21
"""
from loguru import logger

from visualcensus.backend.raspi.const import Key
from visualcensus.frontend.BaseWindow import BaseWindow
from .ui_login_win import Ui_MainWindow


class LoginWindow(BaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)

        self.setupUi(self)
        self.initial()

    def initial(self):
        # 当用户鼠标焦点在输入框且输入信息时，提示信息消失
        self.lineEdit_userName.setPlaceholderText("请输入用户名")
        from visualcensus.backend.raspi.tasks import task_remoter
        task_remoter.signal_button_clicked.connect(self.onRemoterPressed)

    def onRemoterPressed(self, key: Key):
        if key in (Key.KEY_0, Key.KEY_1, Key.KEY_2, Key.KEY_3,
                   Key.KEY_4, Key.KEY_5, Key.KEY_6, Key.KEY_7,
                   Key.KEY_7, Key.KEY_8, Key.KEY_9):
            s = self.lineEdit_userName.text()
            self.lineEdit_userName.setText(s + str(key))
        elif key == Key.KEY_OK:
            from visualcensus.frontend.testwindow import TestWindow
            nextWindow = TestWindow()
            nextWindow.show()
            self.close()
