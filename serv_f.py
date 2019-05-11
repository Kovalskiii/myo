
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

ServoAng1=180   #мизинец
ServoAng2=180
ServoAng3=180
ServoAng4=180
ServoAng5=30


# long map(long x, long in_min, long in_max, long out_min, long out_max)
# pulse = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
# pulse2 = map(ServoAng2,0, 180, SERVOMIN,SERVOMAX)

pulse1 = (ServoAng1 - 0) * (servo_max - servo_min) // (180 - 0) + servo_min
pulse2 = (ServoAng2 - 0) * (servo_max - servo_min) // (180 - 0) + servo_min
pulse3 = (ServoAng3 - 0) * (servo_max - servo_min) // (180 - 0) + servo_min
pulse4 = (ServoAng4 - 0) * (servo_max - servo_min) // (180 - 0) + servo_min
pulse5 = (ServoAng5 - 0) * (servo_max - servo_min) // (180 - 0) + servo_min


pwm.set_pwm(1, 0, pulse1)
pwm.set_pwm(2, 0, pulse2)   
pwm.set_pwm(3, 0, pulse3)    
pwm.set_pwm(4, 0, pulse4)     
pwm.set_pwm(5, 0, pulse5)
    #  time.sleep(1)
