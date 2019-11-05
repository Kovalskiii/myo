import time
from adafruit_servokit import ServoKit
from stuff import Gesture

kit = ServoKit(channels=16)
servos = [kit.servo[i] for i in range(1, 6)]

gestures = {
     Gesture.Rest: (30, 30, 30, 30, 30),
    Gesture.Fist: (180, 180, 180, 180, 40),
    Gesture.Fuck: (180, 180, 5, 180, 20),
    Gesture.Like: (180, 180, 180, 180, 10),
    Gesture.Peace: (180, 180, 20, 20, 170),
    Gesture.Ring: (30, 180, 30, 30, 30),
    Gesture.Middle: (30, 40, 180, 40, 30),
    Gesture.Index: (30, 30, 30, 180, 20),
    Gesture.Thumb: (30, 30, 30, 30, 175),
}

def set_angles(angles, inverse=(2, 5)):
    for i, (s, a) in enumerate(zip(servos, angles), 1):
        angle_to_set = a if not i in inverse else 180 - a 
        # print(angle_to_set)
        s.angle = angle_to_set

def gesture_callback(d):
    if d not in gestures:
        return
    angles = gestures[d]
    print(angles)
    set_angles(angles)

if __name__ == '__main__':
    for gesture, angles in gestures.items():
        print("Testing ", gesture, angles)
        set_angles(angles)
        time.sleep(1)
