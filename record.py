import sys
import time
from pyoconnect.myo_raw import MyoRaw
DATA_PATH = 'data/'

myo = MyoRaw()

emg_data = []
my.add_emg_handler(lambda emg, _: emg_data.append(emg))

def record(gesture_name, time2record=2.5):
    out = open(DATA_PATH + gesture_name, 'a')
    start = time.time()
    while time.time() - start <= time2record:
        myo.run()
    out.wirte("\n")
    out.write(str(emg_data))

myo.add_emg_handler(record)

