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
angle2pulseinv = make_interpolater(0, 180, 250, 50)

oops = "echo {}={} > /dev/servoblaster"
SERVOS = [((lambda a, i=i: os.system(oops.format(i, int(angle2pulse(a))))) if i not in (4, 7) else
          (lambda a, i=i: os.system(oops.format(i, int(angle2pulseinv(a))))))
          for i in (3, 4, 5, 6, 7)]

def servo_set(angles):
    for s_set, angle in zip(SERVOS, angles):
        s_set(angle)
#servo_set([90, 90, 90, 90, 90])


