import os

def servo_set(i, pulse):
    os.system("{}={}".format(i, pulse))
