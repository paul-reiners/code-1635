import pandas as pd
import matplotlib.pyplot as plt
import sys


def plot_data(generation_count):
    rule = 1635
    input_file_path = "out/compression/{}_{:05d}_compression.txt".format(rule, generation_count)
    df = pd.read_csv(input_file_path)
    df = df.iloc[50:]
    print(df)
    df.plot(kind='scatter', x='generation', y='compression-ratio', color='red')
    plt.savefig('img/{}_{:05d}_compression.png'.format(rule, generation_count))
    plt.show()


if __name__ == "__main__":
    n = int(sys.argv[1])
    plot_data(n)
