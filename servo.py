
from board import SCL, SDA
import busio

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# This example also relies on the Adafruit motor library available here:
# https://github.com/adafruit/Adafruit_CircuitPython_Motor
from adafruit_motor import servo
from pyoconnect.myo_raw import Pose

i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
pca.frequency = 60

servos = [servo.Servo(pca.channels[i], min_pulse=125, max_pulse=575) 
          for i in range(1, 6)]

gestures = {
    Pose.REST: (20, 50, 30, 30, 30, 0),
    Pose.FIST: (180, 180, 180, 180, 35, 0),
    Pose.FINGERS_SPREAD: (0, 0, 0, 0, 0, 0),
}


def gesture_callback(d):
    if d not in gestures:
        return
    angles = gestures[d]
    for s, a in zip(servos, angles):
        s.angle = a
