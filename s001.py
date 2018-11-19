# Multiples of 3 and 5

# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time
from timeit import default_timer as timer

starttime = timer()
import cProfile


def compute():
	ans = sum(x for x in range(1000)if (x % 3 == 0 or x % 5 == 0))

	return str(ans)


if __name__ == "__main__":
	print("Answer is:- ", compute())

endtime = timer()
print("Time required for program :-", endtime - starttime)

cProfile.run('compute()')
