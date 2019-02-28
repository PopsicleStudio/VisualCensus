from loguru import logger
from .const import *
import RPi.GPIO as GPIO


def gpio_init():
    logger.debug("GPIO init...")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_IR_REMOTE_CONTROL, GPIO.IN, GPIO.PUD_UP)
