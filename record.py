import sys
import time
from pyoconnect.myo_raw import MyoRaw
DATA_PATH = 'data'

myo = MyoRaw()
emg_data = []
myo.add_emg_handler(lambda emg, _: emg_data.append(emg))

def record(gesture_name, write_to=DATA_PATH, time2record=2.5):
    myo.connect()
    start = time.time()
    while time.time() - start <= time2record:
        myo.run()
    with open(write_to, 'a') as out:
        out.write("\n")
        out.write(gesture_name)
        out.write(str(emg_data))
    emg_data.clear()

if __name__ == '__main__':
    record(*sys.argv[1:])