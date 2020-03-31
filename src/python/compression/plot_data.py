import pandas as pd
import matplotlib.pyplot as plt
import sys


def plot_data(generation_count, gen0=None):
    rule = 1635
    if gen0 is None:
        input_file_path = "out/compression/{}_{:05d}_compression.txt".format(rule, generation_count)
    else:
        input_file_path = "out/compression/{}_{:05d}_{}_compression.txt".format(rule, generation_count, gen0)
    df = pd.read_csv(input_file_path)
    df = df.iloc[50:]
    print(df)
    df.plot(kind='scatter', x='generation', y='compression-ratio', color='red')
    if gen0 is None:
        output_file_path = 'img/{}_{:05d}_compression.png'.format(rule, generation_count)
    else:
        output_file_path = 'img/{}_{:05d}_{}_compression.png'.format(rule, generation_count, gen0)
    plt.savefig(output_file_path)
    plt.show()


if __name__ == "__main__":
    n = int(sys.argv[1])
    if len(sys.argv) == 2:
        plot_data(n)
    else:
        seed = sys.argv[2]
        plot_data(n, seed)
