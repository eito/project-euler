#!/usr/bin/env python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(n):
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

def factors(n):    
  return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
  
largest=0
for i in factors(600851475143):
  if is_prime(i):
    if i > largest:
      largest=i
print largest