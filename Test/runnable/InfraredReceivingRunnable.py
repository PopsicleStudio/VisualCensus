# _*_ coding: utf-8 _*_

"""
Created on 2019/02/27
@author: Moilk
@description: 接收红外遥控的线程
"""
from enum import unique, Enum

from PyQt5.QtCore import QObject


@unique
class Keys(Enum):
    """There is keyValue"""
    KEY_1       =   0x45
    KEY_2       =   0x46
    KEY_3       =   0x47
    KEY_4       =   0x44
    KEY_5       =   0x40
    KEY_6       =   0x43
    KEY_7       =   0x07
    KEY_8       =   0x15
    KEY_9       =   0x09
    KEY_STAR    =   0x16
    KEY_0       =   0x19
    KEY_POUND   =   0x0d
    KEY_UP      =   0x18
    KEY_LEFT    =   0x08
    KEY_OK      =   0x1c
    KEY_RIGHT   =   0x5a
    KEY_DOWN    =   0x52

class InfraredReceivingRunnable(QObject):

    def run(self):
        while True:
            if GPIO.input(PIN) == 0:
                count = 0
                while GPIO.input(PIN) == 0 and count < 200:
                    count += 1
                    time.sleep(0.00006)

                count = 0
                while GPIO.input(PIN) == 1 and count < 80:
                    count += 1
                    time.sleep(0.00006)

                idx = 0
                cnt = 0
                data = [0, 0, 0, 0]
                for i in range(0, 32):
                    count = 0
                    while GPIO.input(PIN) == 0 and count < 15:
                        count += 1
                        time.sleep(0.00006)

                    count = 0
                    while GPIO.input(PIN) == 1 and count < 40:
                        count += 1
                        time.sleep(0.00006)

                    if count > 8:
                        data[idx] |= 1 << cnt
                    if cnt == 7:
                        cnt = 0
                        idx += 1
                    else:
                        cnt += 1
                if data[0] + data[1] == 0xFF and data[2] + data[3] == 0xFF:
                    print("Get the key: 0x%02x" % data[2])
                    exec_cmd(data[2])