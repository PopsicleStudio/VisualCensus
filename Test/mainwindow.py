from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMainWindow

from ui_mainwindow import Ui_MainWindow
from view.EView import EView
from view.SvgView import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.e_view = EView()

        self.setupUi(self)
        self.init_view()

    def init_view(self):
        # self.showFullScreen()
        pal = QPalette(self.palette())
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.layoutImg.addWidget(self.e_view)
        self.e_view.setSizeByVision(EView.F_5_3)
