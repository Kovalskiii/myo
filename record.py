import sys
import time
from pyoconnect.myo_raw import MyoRaw
DATA_PATH = 'data/'

myo = MyoRaw()
myo.connect()
emg_data = []
myo.add_emg_handler(lambda emg, _: emg_data.append(emg))

def record(gesture_name, time2record=2.5):
    start = time.time()
    while time.time() - start <= time2record:
        myo.run()
    with open(DATA_PATH + gesture_name, 'a+') as out:
        out.write("\n")
        out.write(str(emg_data))
    emg_data.clear()

myo.add_emg_handler(record)
