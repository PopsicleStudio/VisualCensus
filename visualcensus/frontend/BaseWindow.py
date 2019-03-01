# _*_ coding: utf-8 _*_

"""
自定义窗口基类
"""
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow
from loguru import logger

from visualcensus.backend.raspi.const import Key


class BaseWindow(QMainWindow):
    signal_send_msg = pyqtSignal(QMainWindow, object)

    def __init__(self, flags, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)
        from visualcensus.backend.raspi.tasks import task_remoter
        task_remoter.signal_button_clicked.connect(self.onRemoterPressed)

    def sendMessage(self, windowFrom, msg):
        self.signal_send_msg.emit(self, msg)

    def onMessageReceived(self, windowFrom, msg):
        pass

    def onRemoterPressed(self, key: Key):
        logger.debug('Get the key: {}'.format(key))
