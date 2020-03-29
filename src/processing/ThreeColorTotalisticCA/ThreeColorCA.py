class ThreeColorCA:
    def __init__(self, r_n):
        self.rule_width = 7
        r = self.convert_number_to_ruleset(r_n)
        # self.convert_ruleset_to_number(r)
        self.rules = r  # List that stores the ruleset,
        self.scl = 1    # How many pixels wide/high is each cell?
        self.cells = [0] * int(width / self.scl)
        self.restart()  # Sets self.generation to 0, only middle cell to 1
        
    def convert_ruleset_to_number(self, rule_set):
        print("rule_set:", rule_set)
        rule_set.reverse()
        number = rule_set[0]
        for i in rule_set[1:]:
            number += i
            number *= 3
        print("number: ", number)
        return number
        
    def convert_number_to_ruleset(self, number):
        rule_set = [0] * self.rule_width
        n = number
        for i in range(self.rule_width):
            rule_set[i] = n % 3
            n = n // 3
        rule_set.reverse()
        print("number: ", number)
        print("rule_set:", rule_set)
        return rule_set

    # Set the rules of the CA
    def setRules(self, r):
        self.rules = r

    # Make a random ruleset
    def randomize(self):
        for i in range(7):
            self.rules[i] = int(random(3))
        print('rule_set:', self.rules)

    # Reset to generation 0
    def restart(self):
        for i in range(len(self.cells)):
            self.cells[i] = 0

        # We arbitrarily start with just the middle cell having a state of "1"
        self.cells[len(self.cells) / 2] = 1
        self.generation = 0

    # The process of creating the new generation
    def generate(self):
        # First we create an empty array for the new values
        nextgen = [0] * len(self.cells)
        # For every spot, determine new state by examing current state,
        # and neighbor states
        # Ignore edges that only have one neighor
        for i in range(1, len(self.cells) - 1):
            left = self.cells[i - 1]     # Left neighbor state
            me = self.cells[i]           # Current state
            right = self.cells[i + 1]    # Right neighbor state
            # Compute next generation state based on ruleset
            nextgen[i] = self.executeRules(left, me, right)

        # Copy the array into current value
        for i in range(1, len(self.cells) - 1):
            self.cells[i] = nextgen[i]

        self.generation += 1

    # This is the easy part, just draw the cells, 
    # fill 255 for '1', fill 0 for'0'
    def render(self):
        scl = self.scl
        for i in range(len(self.cells)):
            cell = self.cells[i]
            if (cell == 2):
                fill(0)
            elif (cell == 1):
                fill(127)
            else:
                fill(255)

            noStroke()
            rect(i * scl, self.generation * scl, scl, scl)

    # Implementing the Wolfram rules
    def executeRules(self, a, b, c):
        total = a + b + c
        if 0 <= total and total <= 7:
            return self.rules[7 - total - 1]
        else:
            return 0

    # The CA is done if it reaches the bottom of the screen
    def finished(self):
        if self.generation > height / self.scl:
            return True
        else:
            return False
