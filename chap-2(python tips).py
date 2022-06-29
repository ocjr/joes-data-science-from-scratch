# The pound sign marks the start of a comment. Python
# ignores the comments, but they're helpful for anyone reading the code.

for i in [1, 2, 3, 4, 5]:
    print(i)                                # first line in "for i" block
    for j in [1, 2, 3, 4, 5]:
        print(j)                            # first line in "for j" block
        print(i + j)                        # last line in "for j" block
    print(i)                                # last line in "for i" block
print("done looping")

# White space is ignored inside parantheses and brackets
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
                           13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

# backslashs indicate that statement contiues onto the next line
two_plus_three = 2 + \
                 3

# Option 1 for imports:
import re
my_regex = re.compile("[0-9]+", re.I)

# Option 2 for imports:
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

# Option 3 for imports: 
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

#Option 4 for imports 
"""Never do this!!!"""
from re import *




# Object-Oriented Programming:
class CountingClicker:
    """A class can/should have a docstring, just like a function"""

    def __init__(self, count = 0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, num_times = 1):
        """Click the clicker some number of times"""
        self.count += num_times

    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0

class NoResetClicker(CountingClicker):
    """ This class has all the same methods as CountingClicker"""

    """ Except that it has a reset method that does nothing."""
    def reset(self):
        pass





