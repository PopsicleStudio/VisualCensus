# _*_ coding: utf-8 _*_

import math
import random

from PyQt5.QtCore import QSizeF, QSize
from .SvgView import *
from .E import *


def __get_edge_by_alpha(alpha: float):
    return math.pi * EView.distance * alpha / 2160


class EView(SvgView):
    DRC = (-90, 90, 180, 0)
    UP, DOWN, LEFT, RIGHT = DRC

    F_3_7, F_3_8, F_3_9, F_4_0, F_4_1, F_4_2, F_4_3, F_4_4, F_4_5, \
    F_4_6, F_4_7, F_4_8, F_4_9, F_5_0, F_5_1, F_5_2, F_5_3 = range(0, 17)
    FIVE_MAP = (3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3)
    DECIMAL_MAP = (0.05, 0.06, 0.08, 0.1, 0.12, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0)

    def __init__(self, resolution=QSize(1920, 1080), dimension=QSizeF(531.5, 299.0), distance=5000.0, parent=None):
        super(EView, self).__init__(parent)

        self.resolution = resolution
        self.dimension = dimension
        self.distance = distance
        self.direction = EView.RIGHT
        self.size_code = EView.F_5_3

        self.openFile(QFile(':/svg/e'))
        self._setSize()

    def up(self):
        self.direction = EView.UP
        self.setDirection()

    def down(self):
        self.direction = EView.DOWN
        self.setDirection()

    def left(self):
        self.direction = EView.LEFT
        self.setDirection()

    def right(self):
        self.direction = EView.RIGHT
        self.setDirection()

    def randomDirection(self):
        self.direction = random.choice(EView.DRC)
        self.setDirection()

    def setDirection(self, direction=None):
        if direction and direction in EView.DRC:
            self.direction = direction

        self._setAngle(self.direction)

    # 根据视力设置E的大小, 5分记录
    def setSizeCode(self, code: int):
        if code in range(0, 17):
            self.size_code = code
            self._setSize()

    def _setSize(self):
        decimal = EView.DECIMAL_MAP[self.size_code]
        edge = math.pi * self.distance / (decimal * 2160)  # 视标实际边长
        # 根据屏幕物理尺寸和分辨率算出视标的分辨率
        e_resolution_w = edge * self.resolution.width() / self.dimension.width()
        e_resolution_h = edge * self.resolution.height() / self.dimension.height()
        super()._setSize(e_resolution_w, e_resolution_h)
