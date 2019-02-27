#!/usr/bin/python  
# -*- coding:utf-8 -*-  
import RPi.GPIO as GPIO
import time
from Constants import Keys

PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, GPIO.PUD_UP)
print("irm test start...")


def exec_cmd(key_val):
    if key_val == Keys.KEY_1:
        print("Button KEY_1")
    elif key_val == Keys.KEY_2:
        print("Button KEY_2")
    elif key_val == Keys.KEY_3:
        print("Button KEY_3")
    elif key_val == Keys.KEY_4:
        print("Button KEY_4")
    elif key_val == Keys.KEY_5:
        print("Button KEY_5")
    elif key_val == Keys.KEY_6:
        print("Button KEY_6")
    elif key_val == Keys.KEY_7:
        print("Button KEY_7")
    elif key_val == Keys.KEY_8:
        print("Button KEY_8")
    elif key_val == Keys.KEY_9:
        print("Button KEY_9")
    elif key_val == Keys.KEY_0:
        print("Button 0")
    elif key_val == Keys.KEY_STAR:
        print("Button KEY_STAR")
    elif key_val == Keys.KEY_POUND:
        print("Button KEY_POUND")
    elif key_val == Keys.KEY_UP:
        print("Button KEY_UP")
    elif key_val == Keys.KEY_LEFT:
        print("Button KEY_LEFT")
    elif key_val == Keys.KEY_OK:
        print("Button KEY_OK")
    elif key_val == Keys.KEY_RIGHT:
        print("Button KEY_RIGHT")
    elif key_val == Keys.KEY_DOWN:
        print("Button KEY_DOWN")


try:
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
except KeyboardInterrupt:
    GPIO.cleanup()
