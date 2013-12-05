#!/usr/bin/env python

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def gen_primes():
  D = {}
  q = 2  # first integer to test for primality.
 
  while True:
    if q not in D:
      # not marked composite, must be prime  
      yield q 
 
      #first multiple of q not already marked
      D[q * q] = [q] 
    else:
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      # no longer need D[q], free memory
      del D[q]
    q += 1

counter=1
primes=gen_primes()
for p in primes:
  if counter == 10001:
    print p
    break
  counter+=1