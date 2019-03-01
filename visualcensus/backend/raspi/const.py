from enum import Enum, unique

PIN_IR_REMOTE_CONTROL = 18


@unique
class Key(Enum):
    """There is keyValue"""
    KEY_UNKNOWN = 0x00
    KEY_1 = 0x45
    KEY_2 = 0x46
    KEY_3 = 0x47
    KEY_4 = 0x44
    KEY_5 = 0x40
    KEY_6 = 0x43
    KEY_7 = 0x07
    KEY_8 = 0x15
    KEY_9 = 0x09
    KEY_STAR = 0x16
    KEY_0 = 0x19
    KEY_POUND = 0x0d
    KEY_UP = 0x18
    KEY_LEFT = 0x08
    KEY_OK = 0x1c
    KEY_RIGHT = 0x5a
    KEY_DOWN = 0x52

    def __str__(self):
        return self.name[4:]

    def __int__(self):
        if self in (Key.KEY_0, Key.KEY_1, Key.KEY_2,
                    Key.KEY_3, Key.KEY_4, Key.KEY_5,
                    Key.KEY_6, Key.KEY_7, Key.KEY_8, Key.KEY_9):
            return int(str(self))
        return self.value
