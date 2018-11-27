# Smallest multiple

# Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


#```logic```
# The smallest number n that is evenly divisible by every number in a set {k1, k2, ..., k_m}
# is also known as the lowest common multiple (LCM) of the set of numbers.
# The LCM of two natural numbers x and y is given by LCM(x, y) = x * y / GCD(x, y).
# When LCM is applied to a collection of numbers, it is commutative, associative, and idempotent.
# Hence LCM(k1, k2, ..., k_m) = LCM(...(LCM(LCM(k1, k2), k3)...), k_m).


import time
from timeit import default_timer as timer

starttime = timer()
import cProfile

import fractions

def compute():
	ans = 1
	for i in range(1, 21):
		ans *= i // fractions.gcd(i, ans)
	return str(ans)


if __name__ == "__main__":
	print("Answer is :-", compute())


endtime = timer()
print("Time required for program :-", endtime - starttime)

cProfile.run('compute()')



