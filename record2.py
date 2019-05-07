import sys
import time
from pyoconnect.myo_raw import MyoRaw
import threading
from stuff import Gesture
import itertools


myo = MyoRaw()
emg_data = []
recording = False
@myo.add_emg_handler
def record(*args):
    if recording:
        emg_data.append(args[0])

connected = False
def myo_run():
    global connected
    myo.connect()
    connected = True
    while True:
        myo.run()


if __name__ == '__main__':
    myo_thread = threading.Thread(target=myo_run, daemon=True)
    myo_thread.start()
    while not connected:
        pass
    write_to = input("File to write: ")
    time2record = float(input("Time to record: "))
    
    for gesture in stuff.Gesture:
        gesture_name = gesture.name
        input("Show {} and press enter".format(gesture_name))
        print("Recording...")
        recording = True
        time.sleep(time2record)
        recording = False
        with open(write_to, 'a') as out:
            out.write(gesture_name)
            out.write(' ')
            out.write(str(emg_data))
            out.write('\n')
            print("Flushed {} of samples for {}".format(len(emg_data), gesture_name))
        emg_data.clear()