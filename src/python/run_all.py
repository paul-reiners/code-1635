import sys

from compression.create_data import create_data
from compression.plot_data import plot_data
from three_state_totalistic_ca import write_ca


def main(num_generations):
    write_ca(num_generations)
    create_data(num_generations)
    plot_data(num_generations)


if __name__ == "__main__":
    n = int(sys.argv[1])
    main(n)
