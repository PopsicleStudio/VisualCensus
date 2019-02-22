from PyQt5.QtCore import QSizeF, QSize
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMainWindow

from ui_mainwindow import Ui_MainWindow
from view.EView import EView
from view.SvgView import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

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

    # 鼠标点击事件
    def onEViewClicked(self, event: QMouseEvent):
        self.e_view.randomDirection()

    # 鼠标滚轮响应事件
    def onWheelEvent(self, event: QWheelEvent):
        size = self.e_view.size_code

        # 鼠标动一格120度
        size += event.angleDelta().y() // 120

        self.e_view.setSizeCode(size)
