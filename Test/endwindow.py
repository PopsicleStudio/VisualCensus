'''
包的说明： 结束界面
时间： 2019年2月26日15:41:23
'''
from PyQt5.QtWidgets import QMainWindow
from ui_end_win import Ui_MainWindow


class EndWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(EndWindow, self).__init__(self)

        self.setupUi(self)