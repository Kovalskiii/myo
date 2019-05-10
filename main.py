from pyoconnect.myo_raw import MyoRaw
import sys
import gesture
import tensorflow as tf
from servo import gesture_callback

if __name__ == '__main__':
    m = MyoRaw()
    gee = gesture.Gesturee(tf.keras.models.load_model(sys.argv[1]))
    # m.add_pose_handler(print)
    # m.add_pose_handler(gesture_callback)
    m.add_emg_handler(gee.emg_handle)
    gee.gesture_handlers.extend(
        [gesture_callback, print]
    )

    m.connect()

    try:
        while True:
            m.run(1)
    except KeyboardInterrupt:
        m.disconnect()
