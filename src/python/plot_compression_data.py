import pandas as pd
import matplotlib.pyplot as plt
import sys


def plot_data(file_path):
    df = pd.read_csv(file_path)
    print(df)
    df.plot(kind='scatter', x='generation', y='compression-ratio', color='red')
    plt.show()


if __name__ == "__main__":
    rule = 1635
    n = sys.argv[1]
    input_file_path = "out/{}_{}_compression.txt".format(rule, n)
    plot_data(input_file_path)
