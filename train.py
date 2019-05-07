import model
import data
import sys


def main(model_save, data_file, epochs=100):
    x, y = data.load(data_file)
    m = model.create_model()
    m.fit(x, y, epochs=int(epochs))
    m.save(model_save)


if __name__ == '__main__':
    main(*sys.argv[1:])
