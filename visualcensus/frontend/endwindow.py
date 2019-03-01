'''
包的说明： 结束界面
时间： 2019年2月26日15:41:23
'''
from PyQt5.QtCore import pyqtSignal, Qt

from visualcensus.backend.raspi.const import Key
from visualcensus.frontend.BaseWindow import BaseWindow
from .ui_end_win import Ui_MainWindow


class EndWindow(BaseWindow, Ui_MainWindow):
    return_login_event = pyqtSignal()

    def __init__(self, vision_value):
        super(EndWindow, self).__init__()

        self.vision_test_value = vision_value
        self.return_login_flag = 0

        self.setupUi(self)
        self.initial()

    def initial(self):
        self.label_result.setText(str(self.vision_test_value))
        # self.label_result.adjustSize()

    def keyPressEvent(self, event):
        # 按数字零返回登录界面
        if event.key() == Qt.Key_0:
            self.return_login_event.emit()

    def onRemoterPressed(self, key: Key):
        from visualcensus.frontend.loginwindow import LoginWindow
        nextWindow = LoginWindow()
        nextWindow.show()
        self.close()
