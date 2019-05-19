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
        self.freq = freq
    
    def set_angle(self, angle):
        duty = angle / 18 + 2
        self.pwm.ChangeDutyCycle(duty)
    
    def __del__(self):
        self.pwm.stop()

    def __repr__(self):
        return "Servo(pin={}, freq={})".format(self.pin, self.freq)

class InvertedServo(Servo):
    def set_angle(self, angle):
        super().set_angle(180 - angle)

atexit.register(GPIO.cleanup)


servos = [
    Servo(29),
    InvertedServo(31),
    Servo(33),
    Servo(35),
    InvertedServo(37),
]

for servo, angle in zip(servos, sys.argv[1:]):
    print(servo)
    sleep(.05)
    servo.set_angle(int(angle))

sleep(1)
