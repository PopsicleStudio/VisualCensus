import sys

from PyQt5.QtWidgets import QApplication

from visualcensus.frontend.launcher import Launcher
from visualcensus.frontend.loginwindow import LoginWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    launcher = Launcher()
    launcher.startWindow(LoginWindow)
    sys.exit(app.exec())
