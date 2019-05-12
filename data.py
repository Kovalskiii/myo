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


def load(file_name, sub_sample_div=10, conf=Config):
    data_dict = _load(file_name)

    x_train, x_test = [], []
    y_train, y_test = [], []

    flat = ((Gesture[gesture.capitalize()].value, data)
            for gesture in data_dict for data in data_dict[gesture])

    for label, sample in flat:
        sub_samples = [sample[i:i+conf.SAMPLE_SIZE]
                       for i in range(0, len(sample) - conf.SAMPLE_SIZE, conf.SAMPLE_SIZE//sub_sample_div)]

        train, test = sub_samples[::2], sub_samples[1::2]

        x_train.extend(train)
        x_test.extend(test)

        y_train.extend([label] * len(train))
        y_test.extend([label] * len(test))

    x_train = np.array(x_train) / conf.EMG_MAX
    x_test = np.array(x_test) / conf.EMG_MAX

    y_train = np.array(y_train)
    y_test = np.array(y_test)

    return (x_train, y_train), (x_test, y_test)
    