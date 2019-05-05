from pyoconnect.myo_raw import MyoRaw
# from servo import gesture_callback
m = MyoRaw()

m.add_pose_handler(print)
# m.add_pose_handler(gesture_callback)
m.add_emg_handler(print)
m.connect()

try:
    while True:
        m.run(1)
except KeyboardInterrupt:
    m.disconnect()
