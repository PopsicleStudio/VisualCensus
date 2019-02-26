'''
说明： 显示E的界面
时间： 2019年2月26日15:41:55
贡献者： 张云远
'''
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMainWindow, QWidget

from ui_test_win import Ui_MainWindow
from view.EView import EView
from view.SvgView import *


class TestWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent)

        self.e_view = EView(QSize(1920, 1080), QSizeF(531.5, 299.0), 5000)

        self.setupUi(self)
        self.init_view()

    def init_view(self):
        # self.showFullScreen()

        # 背景设成白色
        pal = QPalette(self.palette())
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        # 添加EView
        self.layoutImg.addWidget(self.e_view)
        # 设置响应事件
        self.e_view.clicked_event.connect(self.onEViewClicked)
        self.e_view.wheel_event.connect(self.onWheelEvent)

        self.show()

    # 鼠标点击事件
    def onEViewClicked(self, event: QMouseEvent):
        self.e_view.randomDirection()

    # 鼠标滚轮响应事件
    def onWheelEvent(self, event: QWheelEvent):
        size = self.e_view.size_code

        # 鼠标动一格120度
        size += event.angleDelta().y() // 120

        self.e_view.setSizeCode(size)