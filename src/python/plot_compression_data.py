import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df = pd.read_csv('/Users/reiners/Dropbox/projects/code-1635/out/1635_256_data.txt')
    print(df)
    df.plot(kind='scatter', x='generation', y='compression-ratio', color='red')
    plt.show()
