import os


def make_interpolater(left_min, left_max, right_min, right_max): 
    # Figure out how 'wide' each range is  
    leftSpan = left_max - left_min  
    rightSpan = right_max - right_min  

    # Compute the scale factor between left and right values 
    scaleFactor = float(rightSpan) / float(leftSpan) 

    # create interpolation function using pre-calculated scaleFactor
    def interp_fn(value):
        return right_min + (value-left_min)*scaleFactor

    return interp_fn

angle2pulse = make_interpolater(0, 180, 50, 250)

SERVOS = 3, 4, 5, 6, 7

def servo_set(angles):
    for s, a in zip(SERVOS, angles):
        os.system("{}={}".format(i, int(angle2pulse(a))))
