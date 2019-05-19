import RPi.GPIO as GPIO
from time import sleep
import atexit

GPIO.setmode(GPIO.BOARD)

GPIO.setup(29, GPIO.OUT)

class Servo:
    def __init__(self, pin, freq=50):
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, freq)
        self.pin = pin        
        self.pwm.start(0)
    
    def set_angle(self, angle):
        duty = angle / 18 + 2
        GPIO.output(self.pin, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(self.pin, False)
        pwm.ChangeDutyCycle(0)
    
    def __del__(self):
        self.pwm.stop()

atexit.register(GPIO.cleanup)


oof = Servo(29)

