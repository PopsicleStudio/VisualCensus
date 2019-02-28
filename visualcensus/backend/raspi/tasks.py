import RPi.GPIO as GPIO
from PyQt5.QtCore import pyqtSignal, QThread, QWaitCondition, QMutex
from loguru import logger

from .const import *


class TaskRemoter(QThread):
    """Read infrared remoter."""
    button_clicked = pyqtSignal(Key)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._isPause = False
        self._isStop = False
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def pause(self):
        self._isPause = True

    def resume(self):
        self._isPause = False
        self.cond.wakeAll()

    def stop(self):
        self._isStop = True

    def run(self):
        logger.debug('Thread id: {}'.format(int(self.currentThreadId())))
        logger.debug('Start read IR remoter...')
        try:
            while True:
                self.mutex.lock()
                if self._isStop:
                    self._isStop = False
                    self.mutex.unlock()
                    break
                if self._isPause:
                    self.cond.wait(self.mutex)

                if GPIO.input(PIN_IR_REMOTE_CONTROL) == 0:
                    count = 0
                    while GPIO.input(PIN_IR_REMOTE_CONTROL) == 0 and count < 200:
                        count += 1
                        self.usleep(60)

                    count = 0
                    while GPIO.input(PIN_IR_REMOTE_CONTROL) == 1 and count < 80:
                        count += 1
                        self.usleep(60)

                    idx = 0
                    cnt = 0
                    data = [0, 0, 0, 0]
                    for i in range(0, 32):
                        count = 0
                        while GPIO.input(PIN_IR_REMOTE_CONTROL) == 0 and count < 15:
                            count += 1
                            self.usleep(60)

                        count = 0
                        while GPIO.input(PIN_IR_REMOTE_CONTROL) == 1 and count < 40:
                            count += 1
                            self.usleep(60)

                        if count > 8:
                            data[idx] |= 1 << cnt
                        if cnt == 7:
                            cnt = 0
                            idx += 1
                        else:
                            cnt += 1
                    if data[0] + data[1] == 0xFF and data[2] + data[3] == 0xFF:
                        k = Key(data[2])
                        logger.debug('Get the key: {}'.format(k))
                        self.button_clicked.emit(k)
                self.mutex.unlock()
        except KeyboardInterrupt:
            self._isStop = False
            self._isPause = False
            GPIO.cleanup()


task_remoter = TaskRemoter()
