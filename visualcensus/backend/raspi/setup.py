from loguru import logger
from .const import *


def gpio_init():
    try:
        import RPi.GPIO as GPIO
    except ImportError:
        logger.debug('Import "RPI.GPIO" failed.')
        return
    logger.debug("GPIO init...")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_IR_REMOTE_CONTROL, GPIO.IN, GPIO.PUD_UP)
