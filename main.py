from pyoconnect.myo_raw import MyoRaw, Arm
import sys
import gesture
from gesture import Gesture
import tensorflow as tf
# # from servo import gesture_callback
#from yas import angles_t
from servo_blaster import servo_set
from stuff import Config

gestures = {
    Gesture.Rest: (40, 40, 40, 40, 40),
    Gesture.Fist: (180, 180, 180, 180, 35),
    Gesture.Fuck: (180, 180, 40, 180, 50),
}

#def yasg(gesture):
#    if gesture in gestures:s

def wow(gesture):
    if gesture in gestures:
        servo_set(gestures[gesture])
#        angles_to_set[:] = gestures[gesture]


def main(model_load=Config.DEFAULT_SAVE):
    m = MyoRaw()
    gee = gesture.Gesturee(tf.keras.models.load_model(model_load))
    # m.add_pose_handler(print)
    # m.add_pose_handler(gesture_callback)
    m.add_emg_handler(gee.emg_handle)
    m.add_arm_handler(lambda arm, dir: (m.disconnect() if arm == Arm.UNKNOWN else None))
    gee.gesture_handlers.extend(
        [print, wow]
    )


    m.connect()
    m.vibrate(2)
    try:
        while True:
            #if not m.is_connected:
            #    m.connect()
            #    m.vibrate(2) 
            m.run()
    except KeyboardInterrupt:
        m.disconnect()


if __name__ == '__main__':
    main(*sys.argv[1:])
