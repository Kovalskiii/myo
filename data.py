from collections import defaultdict
import numpy as np
from stuff import Config, Gesture


def _load(file_name):
    data_dict = defaultdict(list)
    with open(file_name) as f:
        for line in f.readlines():
            gesture_name, data = line.split(' ', 1)
            data_arr = np.array(eval(data))
            if not data_arr.size:
                continue
            data_dict[gesture_name].append(data_arr)

    return data_dict


def load(file_name, sub_sample_div=4, conf=Config):
    data_dict = _load(file_name)

    x_train, x_test = [], []
    y_train, y_test = [], []

    for label, d in data_dict.items():
        g_enum = Gesture[label.capitalize()]
        add_x = [_d[i:i+conf.SAMPLE_SIZE] 
                 for _d in d 
                 for i in range(0, len(_d) - conf.SAMPLE_SIZE, conf.SAMPLE_SIZE//sub_sample_div)]
        
        x_train.extend(add_x[0::2])
        x_test.extend(add_x[1::2])

        y_train.extend([g_enum.value] * len(x_train))
        y_test.extend([g_enum.value] * len(x_test))

    x_train = np.array(x_train) / conf.EMG_MAX
    x_test = np.array(x_test) / conf.EMG_MAX
    
    y_train = np.array(y_train)
    y_test = np.array(y_test)

    return (x_train, y_train), (x_test, 1y_test)
