import RPi.GPIO as GPIO
from time import sleep
import atexit
import sys
# from gesture import Gesture
import threading

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

# gestures = {
#     Gesture.Rest: (20, 50, 30, 30, 30, 0),
#     Gesture.Fist: (180, 180, 180, 180, 35, 0),
#     Gesture.Fuck: (0, 0, 0, 0, 0, 0),
# }

angles_to_set = (0, 0, 0, 0, 0)

def angles_setter(digit_delay=.05, arm_delay=.5):
    while True:
        for servo, angle in zip(servos, angles_to_set):
            servo.set_angle(angle)
            sleep(digit_delay)
        sleep(arm_delay)


servo_thread = threading.Thread(angles_setter)
servo_thread.setDaemon(True)
servo_thread.start()

