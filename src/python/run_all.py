import sys

from compression.create_data import create_data
from compression.plot_data import plot_data
from three_state_totalistic_ca import write_ca


def main(num_generations, seed=None):
    write_ca(num_generations, seed)
    create_data(num_generations, seed=seed)
    plot_data(num_generations, seed)


if __name__ == "__main__":
    n = int(sys.argv[1])
    if len(sys.argv) == 2:
        main(n)
    else:
        main(n, sys.argv[2])
