import pandas as pd
import matplotlib.pyplot as plt
import sys


def plot_data(generation_count):
    rule = 1635
    input_file_path = "out/{}_{}_hamming-distance.txt".format(rule, generation_count)
    df = pd.read_csv(input_file_path)
    print(df)
    df.plot(kind='scatter', x='generation', y='hamming-distance-from-prev-gen', color='red')
    plt.savefig('img/{}_{}_hamming_distance.png'.format(rule, generation_count))
    plt.show()


if __name__ == "__main__":
    n = sys.argv[1]
    plot_data(n)
