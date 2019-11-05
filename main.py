from pyoconnect.myo_raw import MyoRaw, Arm
import sys
import gesture
from gesture import Gesture
import tensorflow as tf

from servo import set_angles as servo_set, gesture_callback
from stuff import Config
from gpiozero import Button
import time
import serial

#       __
#     >(' )
#       )/
#      /(
#     /  `----/
#     \  ~=- /
#   ~^~^~^~^~^~^~^


def main(model_load=Config.DEFAULT_SAVE):
    m = MyoRaw()
    gee = gesture.Gesturee()
    m.add_emg_handler(gee.emg_handle)
    gee.gesture_handlers.extend(
        [print, gesture_callback]
    )


    m.connect()
    m.vibrate(2)
    try:
        while True:
            m.run()
    except KeyboardInterrupt:
        m.disconnect()


if __name__ == '__main__':
    main(*sys.argv[1:])
