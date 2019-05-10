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

    def emg_handle(self, emg, dir=None):
        self.buff.append(emg)
        if len(self.buff) >= self.sample_size:
            _input = np.array([self.buff]) / self.emg_max
            predictions = self.model.predict(_input)
            print(' '.join('{:5.2f}'.format(x) for x in predictions))
            y = Gesture(predictions.argmax())
            for h in self.gesture_handlers:
                h(y)
            self.buff.clear()
