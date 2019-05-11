
import time

# Import the PCA9685 module.


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).


# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 125  # Min pulse length out of 4096
servo_max = 575  # Max pulse length out of 4096

# Set frequency to 60hz, good for servos.


ServoAngs = [180, 180, 180, 180, 30]

def amap(x, in_min, in_max, out_min, out_max, inverse=False):
    if inverse:
        out_min, out_max = out_max, out_min
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

pulses = [amap(angle, 0, 180, servo_min, servo_max, inverse=(i in (2, 5)))
          for i, angle in enumerate(ServoAngs, 1)]


import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

for i, pulse in enumerate(pulses, 1):
    pwm.set_pwm(i, 0, pulse)
