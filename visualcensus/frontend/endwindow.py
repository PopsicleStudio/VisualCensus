'''
包的说明： 结束界面
时间： 2019年2月26日15:41:23
'''
from PyQt5.QtCore import pyqtSignal, Qt

from visualcensus.backend.raspi.const import Key
from visualcensus.frontend.basewindow import BaseWindow
from visualcensus.frontend.testwindow import TestWindow
from .ui_end_win import Ui_MainWindow


class EndWindow(BaseWindow, Ui_MainWindow):
    return_login_event = pyqtSignal()

    def __init__(self, parent=None):
        super(EndWindow, self).__init__(parent)

        self.vision_test_value = 0.0
        self.return_login_flag = 0

        self.setupUi(self)
        self.initial()

    def initial(self):
        self.label_result.setText(str(self.vision_test_value))
        # self.label_result.adjustSize()
        from visualcensus.backend.raspi.tasks import task_remoter
        task_remoter.signal_button_clicked.connect(self.onRemoterPressed)

    def onMessageReceived(self, windowFrom: type, msg: object):
        if windowFrom == TestWindow and isinstance(msg, float):
            self.vision_test_value = msg
            self.label_result.setText(str(self.vision_test_value))

    def keyPressEvent(self, event):
        # 按数字零返回登录界面
        if event.key() == Qt.Key_0:
            self.__gotoLoginWindow()

    def onRemoterPressed(self, key: Key):
        self.__gotoLoginWindow()

    def __gotoLoginWindow(self):
        from visualcensus.frontend.loginwindow import LoginWindow
        self.startWindow(LoginWindow)
        self.hide()
