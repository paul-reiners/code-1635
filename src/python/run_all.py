import sys

from three_state_totalistic_ca import write_ca


def main(num_generations):
    write_ca(num_generations)

if __name__ == "__main__":
    n = int(sys.argv[1])
