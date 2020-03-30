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
        self.m = 2 * gen_count + 1 if m is None else m

        self.array = np.zeros((gen_count, self.m), dtype=np.int8)
        self.next = 0

    def start_single(self):
        """Starts with one cell in the middle of the top row."""
        self.array[0, self.m // 2] = 1
        self.next += 1

    def start_random(self):
        """Start with random values in the top row."""
        self.array[0] = np.random.random(self.m).round()
        self.next += 1

    def start_string(self, s):
        """Start with values from a string of 1s and 0s."""
        # TODO: Check string length
        self.array[0] = np.array([int(x) for x in s])
        self.next += 1

    def loop(self, steps=1):
        """Executes the given number of time steps."""
        for i in range(steps):
            self.step()

    def step(self):
        """Executes one time step by computing the next row of the array."""
        # First we create an empty array for the new values
        a = self.array
        i = self.next
        c = self.generate(a[i - 1])
        a[i] = c
        self.next += 1

    # The process of creating the new generation
    def generate(self, cells):
        # First we create an empty array for the new values
        nextgen = [0] * len(cells)
        # For every spot, determine new state by examing current state,
        # and neighbor states
        # Ignore edges that only have one neighor
        for i in range(1, len(cells) - 1):
            left = cells[i - 1]  # Left neighbor state
            me = cells[i]  # Current state
            right = cells[i + 1]  # Right neighbor state
            # Compute next generation state based on ruleset
            nextgen[i] = self.execute_rules(left, me, right)

        return np.asarray(nextgen, dtype=np.int8)

    # Implementing the Wolfram rules
    def execute_rules(self, a, b, c):
        total = a + b + c
        if 0 <= total <= 7:
            return self.table[7 - total - 1]
        else:
            return 0

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


def draw_ca(rule_num, gen_count=32, fid=None):
    """Makes and prints a 1D, three-state, totalistic CA with a given rule.

    rule: int rule number
    n: number of rows
    """
    ca = TotalisticCell1D(rule_num, gen_count)
    ca.start_single()
    ca.loop(gen_count - 1)
    ca.print_ca(fid=fid)


def write_ca(gen_count=16):
    fid = "out/{}_{}.txt".format(rule, gen_count)
    rule_num = 1635
    draw_ca(rule_num, gen_count, fid)


if __name__ == "__main__":
    rule = 1635
    n = int(sys.argv[1])
    path = "out/{}_{}.txt".format(rule, n)
    write_ca(n)
