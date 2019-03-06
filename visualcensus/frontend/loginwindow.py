"""
类：登录界面
时间： 2019年2月26日15:37:21
"""
from loguru import logger

from visualcensus.backend.raspi.const import Key
from visualcensus.frontend.basewindow import BaseWindow
from .ui_login_win import Ui_MainWindow


class LoginWindow(BaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)

        self.setupUi(self)
        self.initial()

    def initial(self):
        # 当用户鼠标焦点在输入框且输入信息时，提示信息消失
        self.lineEdit_userName.setPlaceholderText("请输入用户名")
        self.pushButton_ok.clicked.connect(self.onButtonOkClicked)

    # 按下遥控器上的ok键关联的事件
    def onRemoterPressed(self, key: Key):
        if key in (Key.KEY_0, Key.KEY_1, Key.KEY_2, Key.KEY_3,
                   Key.KEY_4, Key.KEY_5, Key.KEY_6, Key.KEY_7,
                   Key.KEY_7, Key.KEY_8, Key.KEY_9):
            s = self.lineEdit_userName.text()
            self.lineEdit_userName.setText(s + str(key))
        elif key == Key.KEY_OK:
            from visualcensus.frontend.testwindow import TestWindow
            self.startWindow(TestWindow)
            self.hide()
        elif key == Key.KEY_POUND:
            s = self.lineEdit_userName.text()
            self.lineEdit_userName.setText(s[:-1])

    # 按下登录界面上的OK_button时的关联事件
    def onButtonOkClicked(self):
        from visualcensus.frontend.testwindow import TestWindow
        self.startWindow(TestWindow)
        self.hide()

    def clearUsername(self):
        self.lineEdit_userName.clear()

    def showEvent(self, event):
        """
        调用show函数就会触发本函数
        :param event:
        :return: None
        """
        self.clearUsername()
        super(LoginWindow, self).showEvent(event)
