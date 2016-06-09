import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def generate_dataset(min, max, mean, std, size, delta=2):
    while True:
        dataset = np.random.uniform(min, max, size)
        m = np.mean(dataset)
        s = np.std(dataset)

        if round(mean, delta) == round(m, delta) and round(std, delta) == round(s, delta):
            return dataset

stats = {
    'print': (5, 7, 5.95, 0.81),
    # 'press': (1, 1.5, 1.26, 0.16),
    'cut': (1, 2, 1.55, 0.28),
    # 'sew': (2, 3, 2.51, 0.27),
    # 'package': (1, 2, 1.49, 0.25)
}

datasets = [generate_dataset(*params, size=50, delta=1) for params in stats.values()]

for dataset in datasets:
    print dataset
    print round(np.mean(dataset), 2)
    print round(np.std(dataset), 2)

def main():
    print_dataset   = np.random.uniform(5, 7, 200)
    press_dataset   = np.random.uniform(1, 1.5, 200)
    cut_dataset     = np.random.uniform(1, 2, 200)
    sew_dataset     = np.random.uniform(2, 3, 200)
    package_dataset = np.random.uniform(1, 2, 200)

    print np.std(print_dataset)
    print np.std(press_dataset)
    print np.std(cut_dataset)
    print np.std(sew_dataset)
    print np.std(package_dataset)

    # fig = plt.figure(1)

    # ax = fig.add_subplot(231)
    # ax.set_title('print')
    # ax.hist(print_dataset)

    # ax = fig.add_subplot(232)
    # ax.set_title('press')
    # ax.hist(press_dataset)

    # ax = fig.add_subplot(233)
    # ax.set_title('cut')
    # ax.hist(cut_dataset)

    # ax = fig.add_subplot(234)
    # ax.set_title('sew')
    # ax.hist(sew_dataset)

    # ax = fig.add_subplot(235)
    # ax.set_title('package')
    # ax.hist(package_dataset)

    # plt.show()
