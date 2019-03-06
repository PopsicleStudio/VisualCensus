# _*_ coding: utf-8 _*_

"""
自定义窗口基类
"""
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow


class BaseWindow(QMainWindow):
    signal_start_window = pyqtSignal(type)
    signal_send_message = pyqtSignal(QMainWindow, type, object)
    signal_closed = pyqtSignal(QMainWindow)

    def __init__(self, parent=None):
        super().__init__(parent)

    def startWindow(self, windowType: type):
        self.signal_start_window.emit(windowType)

    def sendMessage(self, window_to: type, msg: object):
        self.signal_send_message.emit(self, window_to, msg)

    def onMessageReceived(self, windowFrom: type, msg: object):
        pass

    def closeEvent(self, *args, **kwargs):
        self.signal_closed.emit(self)

    def showEvent(self, event):
        from visualcensus.backend.raspi.tasks import task_remoter
        task_remoter.signal_button_clicked.connect(self.onRemoterPressed)
        print(str(self)+' show')
        super(BaseWindow, self).showEvent(event)

    def hideEvent(self, event):
        from visualcensus.backend.raspi.tasks import task_remoter
        task_remoter.signal_button_clicked.disconnect(self.onRemoterPressed)
        print(str(self)+' hide')
        super(BaseWindow, self).hideEvent(event)

    def onRemoterPressed(self, key):
        pass
