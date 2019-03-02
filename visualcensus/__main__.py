import sys

from PyQt5.QtWidgets import QApplication
from loguru import logger

from visualcensus.backend.raspi import setup
from visualcensus.backend.raspi.tasks import task_remoter
from visualcensus.const import (
    REQUIRED_PYTHON_VER
)
from visualcensus.frontend.launcher import Launcher
from visualcensus.frontend.loginwindow import LoginWindow


def validate_python():
    """Validate that the right Python version is running."""
    if sys.version_info[:3] < REQUIRED_PYTHON_VER:
        logger.debug("Visual Census requires at least Python {}.{}.{}".format(
            *REQUIRED_PYTHON_VER
        ))
        sys.exit(1)


def main():
    """Start Visual Census."""
    validate_python()
    app = QApplication(sys.argv)
    launcher = Launcher()
    launcher.startWindow(LoginWindow)
    setup.gpio_init()
    task_remoter.start()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
