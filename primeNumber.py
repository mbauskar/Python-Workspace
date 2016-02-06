# find the all the possible prime number from the given integer number

from itertools import permutations, count, islice
from math import sqrt
import time

number = 3657
strNumber = str(number)
listNumbers = []
primeNumbers = []

def is_prime(a):
	# return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    # return all(a % i for i in xrange(2, a))
    return all(a % i for i in xrange(2, a/2))

for i in xrange(1, len(strNumber)+1):
	_list = map(lambda n: int("".join(n)), permutations(strNumber, i))
	listNumbers.extend(_list)

listNumbers = list(set(listNumbers))
listNumbers.sort()

for n in listNumbers:
	if is_prime(n):
		primeNumbers.append(n)

print "count : ", len(primeNumbers)
print "Prime Numbers : ", primeNumbers