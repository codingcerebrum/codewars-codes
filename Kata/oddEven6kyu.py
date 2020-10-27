# Given an integer n return "odd" if the number of its divisors is odd. Otherwise return "even".

# Note: big inputs will be tested.

# Examples:
# All prime numbers have exactly two divisors (hence "even").

# For n = 12 the divisors are [1, 2, 3, 4, 6, 12] – "even".

# For n = 4 the divisors are [1, 2, 4] – "odd".

import math as mt

def oddity(n):
    numrange = int(mt.sqrt(n))
    numlist = []

    for x in range(1,numrange+1):
        if(n % x == 0):
            numlist.append(int(x))
            numlist.append(int(n/x))

    numlist = list(dict.fromkeys(numlist))
    return len(numlist)

n=30
print(oddity(n))
# num = mt.log(n/2) * 2
# print(num)

# hh = [1] * 30
# print(hh)