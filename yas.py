import RPi.GPIO as GPIO
from time import sleep
import atexit
import sys

GPIO.setmode(GPIO.BOARD)


class Servo:
    def __init__(self, pin, freq=50):
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, freq)
        self.pin = pin        
        self.pwm.start(0)
    
    def set_angle(self, angle):
        duty = angle / 18 + 2
        self.pwm.ChangeDutyCycle(duty)
    
    def __del__(self):
        self.pwm.stop()

atexit.register(GPIO.cleanup)


s = Servo(int(sys.argv[1]))
print("Setting angles")
s.set_angle(int(sys.argv[2]))

sleep(1)
