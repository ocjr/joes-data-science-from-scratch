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
from re import T
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


# Iterables and Generators

def generate_range(n):
    i = 0
    while i < n:
        yield i             # Every call to yield produces a value of the generator
        i += 1

evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)


names = ['Alice', 'Bob', 'Charlie','Debbie']

# Not Pythonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# Also not pythonic
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1

# Pythonic
for i, name in enumerate(names):
    print(f"name {i} is {name}")


# Randomness

import random
random.seed(10)             # this ensures we get the same results every time

four_uniform_randoms = [random.random() for _ in range(4)]

[0.5714025946899135,        # random.random() produces numbers
 0.4288890546751146,        # uniformly between 0 and 1
 0.5780913011344704,        # It's the random function we'll use
 0.20609823213950174]       # most often. 

 
random.seed(10)            # set the seed to 10
print(random.random())     # 0.57140259469 
random.seed(10)            # reset the seed to 10
print(random.random())     # 0.57140259469 again


random.randrange(10)        # choose randomly from range(10) = [0,1, ..., 9]
random.randrange(3,6)       # choose randomly from range(3,6) = [3, 4, 5]

up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)
# [2, 6, 7, 10, 4, 9, 1, 3, 5, 8]

my_best_friend = random.choice(['Alice','Bob','Charlie'])   # 'Charlie' for me

lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)         # [23, 2, 26, 55, 8, 38]

four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)                                # [5, 6, 6, 4]

# Regular Expressions

import re

try:
    re_examples = [                                             # All of these are True, becuase
        not re.match('a','cat'),                                # 'cat' doesn't start with 'a'
        re.search('a','cat'),                                   # 'cat' has an 'a' in it
        not re.search('c','dog'),                               # 'dog' doesn't have a 'c' in it
        3 == len(re.split('[ab]', "carbs")),                    # Split on a or b to ['c','r','s']
        'R-D-' == re.sub("[0-9]", "-", "R2D2")                  # Replace digits with dashes
    ]

    assert all(re_examples), "all the regex examples should be true"
except AssertionError as e:
    print(e)


# Functional Programming

# zip and Argument Unpacking

list1 = ['a','b','c']
list2 = [1,2,3]

# zip is lazy, so you have to do something like the following:
[pair for pair in zip(list1, list2)]                            # is [('a',1),('b',2),('c',3)]

# unzip
pairs = [('a',1),('b',2),('c',3)]
letters, numbers = zip(*pairs)                                  # same as letters, number = zip(('a',1),('b',2),('c',3))

def add(a, b): return a + b

add(1,2)                    # returns 3
try:
    add([1,2])
except TypeError:
    print("add expects two inputs")

add(*[1,2])                 # returns 3


#args and kwargs

def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return 2 * f(x)

    # and return that new function
    return g

def f1(x):
    return x + 1

g = doubler(f1)
assert g(3) == 8, "(3 + 1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"

def f2(x, y):
    return x + y

g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("as defined, g only takes one argument")

def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("unnamed kwargs:", kwargs)

magic(1, 2, key="word", key2="word2")

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z":3}
assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should be 6"


def doubler_correct(f):
    """ works no matter what king of inputs f expects"""
    def g(*args, **kwargs):
        """ whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
assert g(1, 2) == 6, "doubler should work now"


# Type Annotations

# Dynamically typed language
def add(a, b):
    return a + b

assert add(10,5) == 15,                     " + is valid for numbers"
assert add([1,2],[3]) == [1,2,3],           " + is valid for lists"
assert add('hi ', 'there') == 'hi there',   " + is valid for strings"

try:
    add(10, 'five')
except TypeError:
    print('cannot add an int to a string')

# Statically typed
def add(a: int, b: int) -> int:
    return a + b

add(10, 5)                  # you'd like this to be ok
add('hi ','there')          # you'd like this to be not ok


from typing import List
def f(xs: List[int]) -> None:
    xs.append


# Type Annotaions

# not the best
def total(xs: list) -> float:
    return sum(total)

# better:
def total(xs: List[float]) -> float:
    return sum(total)

# this how to type-annotate variabls when you define them.
# but this is unnecessary; it's obvious x in and int.
x: int = 5

# But sometimes it isn't so obvious

values = []                 # what's my type?
best_so_far = None          # what's my type?

from typing import Optional

values: List[int] = []
best_so_far: Optional[float] = None     # allowed to be either a float or None

# the type annotations in this snippet are all unnecessary
from typing import Dict, Iterable, Tuple

# key are strings, values are ints
counts: Dict[str, int] = {'data': 1, 'science': 2}

# lists and generators are both iterable
if lazy:
    evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
else:
    evens = [0, 2, 4, 6, 8]

# tuples specify a type for each element
triple: Tuple[int, float, int] = (10, 2.3, 5)

from typing import Callable

# The type hint says the repeater is a function that takes
# two arguments, a string and an int, and returns a string
def twice(repeater: Callable[[str, int], str], s:str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, "type hints") == "type hints, type hints"

