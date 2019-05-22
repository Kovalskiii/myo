import numpy as np
import model
from stuff import Gesture, Config
import threading
from collections import deque
import time
import tensorflow as tf

class Gesturee:
    def __init__(self, model_file=Config.DEFAULT_SAVE, sample_size=Config.SAMPLE_SIZE, emg_max=Config.EMG_MAX, gesture_delay=Config.GESTURE_DELAY):
        self.buff = deque(maxlen=sample_size)
        self.sample_size = sample_size
        self.emg_max = emg_max
        self.gesture_delay = gesture_delay
        self.gesture_handlers = []
        def gesture_thread():
            self.model = tf.keras.models.load_model(model_file)
            while True:
                time.sleep(self.gesture_delay)
                self.detect_gesture()

        self.gesture_thread = threading.Thread(target=gesture_thread)
        self.gesture_thread.setDaemon(True)
        self.gesture_thread.start()

    def emg_handle(self, emg, dir=None):
        self.buff.append(emg)

    def detect_gesture(self):
        if len(self.buff) < self.sample_size:
            return
        print(self.buff)
        _input = np.array([self.buff]) / self.emg_max
        predictions = self.model.predict(_input)
        y = Gesture(predictions.argmax())
        for h in self.gesture_handlers:
            h(y)
