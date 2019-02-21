import math

from view.SvgView import *

import view.E


def __get_edge_by_alpha(alpha: float):
    return math.pi * EView.distance * alpha / 2160


class EView(SvgView):
    resolution = {'w': 1920, 'h': 1080}
    dimension = {'w': 531.5, 'h': 299.0}
    distance = 5000
    UP, DOWN, LEFT, RIGHT = range(1, 5)

    F_3_7, F_3_8, F_3_9, F_4_0, F_4_1, F_4_2, F_4_3, F_4_4, F_4_5, \
        F_4_6, F_4_7, F_4_8, F_4_9, F_5_0, F_5_1, F_5_2, F_5_3 = range(0, 17)
    FIVE_MAP = (3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3)
    DECIMAL_MAP = (0.05, 0.06, 0.08, 0.1, 0.12, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0)

    def __init__(self, parent=None):
        super(EView, self).__init__(parent)

        self.direction = EView.RIGHT

        self.openFile(QFile(':/svg/e'))
        self.setSize(50, 50)

    def up(self):
        self.direction = EView.UP
        self.setAngle(-90)

    def down(self):
        self.direction = EView.DOWN
        self.setAngle(90)

    def left(self):
        self.direction = EView.LEFT
        self.setAngle(180)

    def right(self):
        self.direction = EView.RIGHT
        self.setAngle(0)

    # 根据视力设置E的大小, 5分记录
    def setSizeByVision(self, code: int):
        if code < EView.F_3_7 or code > EView.F_5_3:
            return
        decimal = EView.DECIMAL_MAP[code]
        edge = math.pi * EView.distance / (decimal * 2160)  # 视标实际边长
        # 根据屏幕物理尺寸和分辨率算出视标的分辨率
        e_resolution_w = edge * EView.resolution['w'] / EView.dimension['w']
        e_resolution_h = edge * EView.resolution['h'] / EView.dimension['h']
        self.setSize(e_resolution_w, e_resolution_h)
