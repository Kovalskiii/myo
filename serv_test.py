
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 125  # Min pulse length out of 4096
servo_max = 575  # Max pulse length out of 4096

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

ServoAngs = [20, 50, 30, 30, 30]

def amap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

pulses = [amap(angle, servo_min, servo_max, 0, 180) for angle in ServoAngs]

for i, pulse in enumerate(pulses, 1):
    pwm.setPWM(i, 0, pulse)

time.sleep(1)
