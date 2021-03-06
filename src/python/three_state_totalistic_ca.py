# Author:
# Adapted from code in Think Complexity, 2nd Edition, by by Allen Downey

import sys

import numpy as np

rule_width = 7


def make_table(rule_num):
    """Make the table for a given CA rule.

    rule: int 0-2186

    returns: array of 7 0s, 1s, and 2s
    """
    rule_set = [0] * rule_width
    num = rule_num
    for i in range(rule_width):
        rule_set[i] = num % 3
        num = num // 3
    rule_set.reverse()
    print("number: ", rule_num)
    print("rule_set:", rule_set)
    return rule_set


class TotalisticCell1D:
    """Represents a 1-D, three-state, totalistic cellular automaton"""

    def __init__(self, rule_num, gen_count, m=None):
        """Initializes the CA.

        rule: integer
        n: number of rows
        m: number of columns

        Attributes:
        table:  rule dictionary that maps from triple to next state.
        array:  the numpy array that contains the data.
        next:   the index of the next empty row.
        """
        self.rule_width = 7
        self.table = make_table(rule_num)
        self.n = gen_count
        self.width = 2 * gen_count + 1 if m is None else m

        self.array = np.zeros((gen_count, self.width), dtype=np.int8)
        self.next = 0

    def start_single(self):
        """Starts with one cell in the middle of the top row."""
        self.array[0, self.width // 2] = 1
        self.next += 1

    def start_random(self):
        """Start with random values in the top row."""
        self.array[0] = np.random.random(self.width).round()
        self.next += 1

    def start_string(self, s):
        """Start with values from a string of 1s and 0s."""
        s_len = len(s)
        # Check string length
        assert s_len <= self.width
        padding_len = self.width - s_len
        left_padding_len = padding_len // 2
        ss = "0" * left_padding_len + s
        right_padding_len = self.width - len(ss)
        sss = ss + "0" * right_padding_len
        self.array[0] = np.array([int(x) for x in sss])
        self.next += 1

    def loop(self, steps=1):
        """Executes the given number of time steps."""
        for i in range(steps):
            if i % 1024 == 0:
                print("step {} of {}".format(i, self.n))
            self.step()

    def step(self):
        """Executes one time step by computing the next row of the array."""
        a = self.array
        i = self.next
        window = [1, 1, 1]
        row = self.array[i - 1]
        correlated_row = np.correlate(row, window, mode="same")
        next_row = np.array([self.table[7 - total - 1] for total in correlated_row])
        a[i] = next_row
        self.next += 1

    def print_ca(self, start=0, end=None, fid=None):
        """Prints the CA.

        start: index of the first column to be shown
        end: index of the last column to be shown
        """
        a = self.array[:, start:end]
        if fid:
            np.savetxt(fid, a, delimiter="", fmt='%1d', )
        else:
            for row in a:
                print(row)


def draw_ca(rule_num, gen_count=32, fid=None, start=None):
    """Makes and prints a 1D, three-state, totalistic CA with a given rule.

    rule: int rule number
    n: number of rows
    """
    ca = TotalisticCell1D(rule_num, gen_count)
    if start is None:
        ca.start_single()
    else:
        ca.start_string(start)
    ca.loop(gen_count - 1)
    ca.print_ca(fid=fid)


def write_ca(gen_count=16, start=None):
    rule_num = 1635
    if start is None:
        file_name = "out/ca/{}_{:05d}.txt".format(rule_num, gen_count)
    else:
        file_name = "out/ca/{}_{:05d}_{}.txt".format(rule_num, gen_count, start)
    fid = file_name
    draw_ca(rule_num, gen_count, fid, start)


if __name__ == "__main__":
    n = int(sys.argv[1])
    if len(sys.argv) > 2:
        seed = sys.argv[2]
        write_ca(n, seed)
    else:
        write_ca(n)
