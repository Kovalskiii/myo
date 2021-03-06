from enum import Enum
import os
script_dir = os.path.dirname(__file__)
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
    Rock = 10
    Rasta = 11


class Config:
    SAMPLE_SIZE = 30
    GESTURE_NUM = len(Gesture)
    EMG_MAX = 2048
    EPOCHS = 1000
    DEFAULT_DATA = os.path.join(script_dir, 'data/fresh')
    DEFAULT_SAVE = os.path.join(script_dir, 'saved_models/m')
    GESTURE_DELAY = 0.5
