import model
import data
import sys


def main(model_save, data_file, epochs=100):
    (x, y), (test_x, test_y) = data.load("data/gdata_clean")
    m = model.create_model()
    m.fit(x, y, epochs=int(epochs))
    m.save(model_save)
    m.evaluate(test_x, test_y)


if __name__ == '__main__':
    main(*sys.argv[1:])
