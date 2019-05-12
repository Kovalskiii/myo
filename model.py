import tensorflow as tf
import numpy as np
from stuff import Config, Gesture


def create_model(conf=Config):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(conf.SAMPLE_SIZE, 8)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(conf.GESTURE_NUM, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model
