import sys

from PyQt5.QtWidgets import QApplication

from visualcensus.frontend.loginwindow import LoginWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LoginWindow()
    w.show()
    sys.exit(app.exec())
