# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


import time
from timeit import default_timer as timer

starttime = timer()
import cProfile

import fractions


def compute():
    N = 100
    s = sum(i for i in range(1, N + 1))
    s2 = sum(i ** 2 for i in range(1, N + 1))
    return str(s ** 2 - s2)


if __name__ == "__main__":
    print("Answer is :-", compute())


endtime = timer()
print("Time required for program :-", endtime - starttime)

cProfile.run("compute()")
