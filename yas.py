import RPi.GPIO as GPIO
from time import sleep
import atexit
import sys
# from gesture import Gesture
# import threading

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


test = [
    (20, 50, 30, 30, 30, 0),
    (180, 180, 180, 180, 35, 0),
    (0, 0, 0, 0, 0, 0),
]

while True:
    for angles in test:
        print(angles)
        for servo, angle in zip(servos, angles):
            servo.set_angle(angle)
            sleep(.1)
        sleep(.5)

# angles_to_set = [0, 0, 0, 0, 0]
# def servos_set(gesture):
#     while True:
#     for servo, angle in zip(servos, angles_to_set):
#         sleep(.1)
#         servo.set_angle(anlge)
#         sleep(.5)


# servo_thread = threading.Thread(servos_set)
# servo_thread.setDaemon(True)
# servo_thread.start()

# def servos_gestures_callback(gesture):
#     angles = gestures.get(gesture)
#     if angles is None:
#         continue
#     angles_to_set[:] = angles
