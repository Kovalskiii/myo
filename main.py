from pyoconnect.myo_raw import MyoRaw

m = MyoRaw()

m.add_pose_handler(print)
m.add_emg_handler(print)
m.connect()

try:
    while True:
        m.run(1)
except KeyboardInterrupt:
    m.disconnect()
