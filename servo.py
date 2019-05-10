
# from board import SCL, SDA
# import busio

# Import the PCA9685 module.
# from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit
# This example also relies on the Adafruit motor library available here:
# https://github.com/adafruit/Adafruit_CircuitPython_Motor
# from adafruit_motor import servo
# from pyoconnect.myo_raw import Pose
from stuff import Gesture

# i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
# pca = PCA9685(i2c)
# pca.frequency = 60

# servos = [servo.Servo(pca.channels[i], min_pulse=125, max_pulse=575) 
#           for i in range(1, 6)]

kit = ServoKit(channels=8)
servos = [kit.servo[i] for i in range(1, 6)]

gestures = {
    Gesture.Rest: (20, 50, 30, 30, 30, 0),
    Gesture.Fist: (180, 180, 180, 180, 35, 0),
    Gesture.Fuck: (0, 0, 0, 0, 0, 0),
}


def gesture_callback(d):
    if d not in gestures:
        return
    angles = gestures[d]
    print(angles)
    for s, a in zip(servos, angles):
        s.angle = a
