import numpy as np
import model
from stuff import Gesture, Config


class Gesturee:
    def __init__(self, model, conf=Config):
        self.model = model
        self.buff = []
        self.sample_size = conf.SAMPLE_SIZE
        self.emg_max = conf.EMG_MAX
        self.gesture_handlers = []

    def emg_handle(self, emg, dir):
        self.buff.append(emg)
        if len(self.buff) == self.sample_size:
            y = Gesture(self.model.call(np.array(self.buff)/model.EMG_MAX).argmax())
            for h in self.gesture_handlers:
                h(y)
            self.buff.clear()
