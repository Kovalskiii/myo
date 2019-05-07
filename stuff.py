from enum import Enum

class Gesture(Enum):
    Fist = 0
    Fuck = 1
    Like = 2


class Config:
    SAMPLE_SIZE = 50
    GESTURE_NUM = len(Gesture)
    EMG_MAX = 2048
    EPOCHS = 100
