"""
说明： 显示E的界面
时间： 2019年2月26日15:41:55
贡献者： 张云远
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMainWindow

from .ui_test_win import Ui_MainWindow
from .views.EView import EView
from .views.SvgView import *


class TestWindow(QMainWindow, Ui_MainWindow):
    test_end_event = pyqtSignal()

    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent)

        # 记录用户行为的变量
        self.judge_correct_nums = 0
        self.judge_wrong_nums = 0
        self.user_input_direction = 0
        self.vision_value = 0
        self.test_end_flag = 0

        self.e_view = EView(QSize(1920, 1080), QSizeF(531.5, 299.0), 5000)
        # 必须在view实例化以后访问，否则程序会崩溃
        self.current_direction = self.e_view.direction

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

    def keyPressEvent(self, event):

        # print("按下： " + str(event.key()))
        # 不区分大小写 按键事件对大小写不敏感
        if event.key() == Qt.Key_W:
            self.user_input_direction = EView.UP
        if event.key() == Qt.Key_A:
            self.user_input_direction = EView.LEFT
        if event.key() == Qt.Key_S:
            self.user_input_direction = EView.DOWN
        if event.key() == Qt.Key_D:
            self.user_input_direction = EView.RIGHT

        self.keyhandle()
        # if event.key() == Qt.Key_B:
        #     # 0 代表E字很小， 17 代表E字很大
        #     size = self.e_view.size_code
        #     size += 1
        #
        #     self.e_view.setSizeCode(size)
        # if event.key() == Qt.Key_M:
        #     size = self.e_view.size_code
        #     size -= 1
        #
        #     self.e_view.setSizeCode(size)

    # 键盘的处理函数
    def keyhandle(self):
        # 每次判断之前需要获取当前的方向
        self.current_direction = self.e_view.direction

        if self.current_direction == self.user_input_direction:
            self.judge_correct_nums += 1
            print("correct_nums:" + str(self.judge_correct_nums))
            self.e_view.randomDirection()
            # 当前大小的E方向判断正确次数达三次
            if self.judge_correct_nums > 3:
                size = self.e_view.size_code
                self.vision_value = EView.FIVE_MAP[size]
                # self.test_end_flag = 1
                self.test_end_event.emit()

        else:
            self.judge_wrong_nums += 1
            print("wrong nums:" + str(self.judge_wrong_nums))
            self.e_view.randomDirection()
            size = self.e_view.size_code
            # 尺寸与视力直接相关，越大视力越低
            size -= 1
            if size < 0:
                size = 0
            self.e_view.setSizeCode(size)
            # 当前大小的E方向判断错误次数达三次
            # if self.judge_wrong_nums > 3:
            #     self.judge_wrong_nums = 0
            #     size = self.e_view.size_code
            #     size += 1
            #     self.e_view.setSizeCode(size)
