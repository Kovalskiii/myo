from pyoconnect.myo_raw import MyoRaw
import sys
import gesture
from gesture import Gesture
import tensorflow as tf
# # from servo import gesture_callback
from yas import angles_t
from servo_blaster import servo_seto_set
from stuff import Config

gestures = {
    Gesture.Rest: (20, 50, 30, 30, 30, 0),
    Gesture.Fist: (180, 180, 180, 180, 35, 0),
    Gesture.Fuck: (0, 0, 0, 0, 0, 0),
}

def yasg(gesture):
    if gesture in gestures:s

def wow(gesture):
    if gesture in gestures:
        servo_set(gestures[gesture])
        angles_to_set[:] = gestures[gesture]


def main(model_load=Config.DEFAULT_SAVE):
    m = MyoRaw()
    gee = gesture.Gesturee(tf.keras.models.load_model(model_load))
    # m.add_pose_handler(print)
    # m.add_pose_handler(gesture_callback)
    m.add_emg_handler(gee.emg_handle)
    gee.gesture wowlers.extend(
        [print, yasg]
    )

    m.connect()

    try:
        while True:
            m.run(1)
    except KeyboardInterrupt:
        m.disconnect()


if __name__ == '__main__':
    main(*sys.argv[1:])
