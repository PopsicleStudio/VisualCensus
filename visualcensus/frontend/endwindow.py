'''
包的说明： 结束界面
时间： 2019年2月26日15:41:23
'''
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow
from .ui_end_win import Ui_MainWindow


class EndWindow(QMainWindow, Ui_MainWindow):
    return_login_event = pyqtSignal()

    def __init__(self, vision_value):
        super(EndWindow, self).__init__()

        self.vision_test_value = vision_value
        self.return_login_flag = 0

        self.setupUi(self)
        self.resultDisplay()

    def resultDisplay(self):
        self.show()
        self.label_result.setText(str(self.vision_test_value))
        # self.label_result.adjustSize()

    def keyPressEvent(self, event):
        # 按数字零返回登录界面
        if event.key() == Qt.Key_0:
            self.return_login_event.emit()
