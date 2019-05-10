from enum import Enum

class Gesture(Enum):
    Fist = 0
    Fuck = 1
    Like = 2
    Rest = 3
    Peace = 4
    Pinky = 5
    Ring = 6
    Middle = 7
    Index = 8
    Thumb = 9
    Spider = 10
    Rock = 11
    Rasta = 12


class Config:
    SAMPLE_SIZE = 25
    GESTURE_NUM = len(Gesture)
    EMG_MAX = 2048
    EPOCHS = 100
