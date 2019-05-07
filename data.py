from collections import defaultdict
import numpy as np
from stuff import Config, Gesture


def load(file_name, sub_sample_div=4, conf=Config):
    data_dict = defaultdict(list)
    with open(file_name) as f:
        for line in f.readlines():
            gesture_name, data = line.split(' ', 1)
            data_arr = np.array(eval(data))
            if not data_arr.size:
                continue
            data_dict[gesture_name].append(data_arr)

    x = []
    y = []
    for label, d in data_dict.items():
        g_enum = Gesture[label.capitalize()]
        add_x = [_d[i:i+conf.SAMPLE_SIZE] for _d in d for i in range(0, len(_d) - conf.SAMPLE_SIZE, conf.SAMPLE_SIZE//sub_sample_div)]
        x.extend(add_x)
        y.extend([g_enum] * len(add_x))

    x = np.array(x) / conf.EMG_MAX
    y = np.array([_y.value for _y in y])

    return x, y
