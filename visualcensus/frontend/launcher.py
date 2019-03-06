from PyQt5.QtWidgets import QWidget

from visualcensus.frontend.basewindow import BaseWindow


class Launcher(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__list_window = []

    def startWindow(self, cls):
        if isinstance(cls, type) and issubclass(cls, BaseWindow):
            for x in self.__list_window:
                if isinstance(x, cls):
                    self.__list_window.append(x)
                    self.__list_window.remove(x)
                    x.show()
                    return
            new_window = cls(self)
            new_window.signal_closed.connect(self.onWindowRemoved)
            new_window.signal_send_message.connect(self.passMessage)
            new_window.signal_start_window.connect(self.startWindow)
            self.__list_window.append(new_window)
            self.__list_window[-1].show()

    def onWindowRemoved(self, window):
        if window in self.__list_window:
            self.__list_window.remove(window)

    def passMessage(self, window_from: BaseWindow, window_to: type, msg: object):
        if window_from in self.__list_window:
            for w in self.__list_window:
                if isinstance(w, window_to):
                    w.onMessageReceived(window_from.__class__, msg)
                    return
