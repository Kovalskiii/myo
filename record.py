import sys
import time
from pyoconnect.myo_raw import MyoRaw
import threading

myo = MyoRaw()
emg_data = []
recording = False
@myo.add_emg_handler
def record(*args):
    if recording:
        emg_data.append(args[0])

def myo_run():
    myo.connect()
    while True:
        myo.run()

myo_thread = threading.Thread(target=myo_run, daemon=True)




if __name__ == '__main__':
    write_to = input("File to write:")
    time2record = float(input("Time to record"))
    
    while True:
        gesture_name = input("gesture name:")
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
