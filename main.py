from pyoconnect.myo_raw import MyoRaw
import sys
import gesture
import tensorflow as tf
# from servo import gesture_callback
from yas import servos_gestures_callback
from stuff import Config


def main(model_load=Config.DEFAULT_SAVE):
    m = MyoRaw()
    gee = gesture.Gesturee(tf.keras.models.load_model(model_load))
    # m.add_pose_handler(print)
    # m.add_pose_handler(gesture_callback)
    m.add_emg_handler(gee.emg_handle)
    gee.gesture_handlers.extend(
        [print, servos_gestures_callback]
    )

    m.connect()

    try:
        while True:
            m.run(1)
    except KeyboardInterrupt:
        m.disconnect()


if __name__ == '__main__':
    main(*sys.argv[1:])
