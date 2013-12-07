#!/usr/bin/env python

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

total=0
for prime in gen_primes():
  if prime > 2000000:
    print total
    break
  total+=prime
