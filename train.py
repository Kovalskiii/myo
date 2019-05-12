import model
import data
import sys
import tensorflow as tf
from stuff import Config


def main(data_file=Config.DEFAULT_DATA, model_save=Config.DEFAULT_SAVE,
         epochs=Config.EPOCHS):
    (x, y), (test_x, test_y) = data.load(data_file)

    try:
        m = tf.keras.models.load_model(model_save)
    except OSError:
        m = model.create_model()

    checkpointer = tf.keras.callbacks.ModelCheckpoint(
        filepath=model_save,
        save_best_only=True,
        verbose=1)
    m.fit(x, y, validation_data=(test_x, test_y),  epochs=int(epochs),
          callbacks=[checkpointer])


if __name__ == '__main__':
    main(*sys.argv[1:])
