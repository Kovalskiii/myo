import os

def servo_set(i, pulse):
    os.system("echo {}={} > /dev/servoblaster".format(i, pulse))
