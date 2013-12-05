#!/usr/bin/env python

"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(s=""):
  i=0
  while s[i] == s[len(s)-1-i]:
    i+=1
    if i > len(s)/2:
      return True
  return False

largest=0
for x in xrange(100,1000):
  for y in xrange(100,1000):
    p=x*y
    s=str(p)
    if s[0] == s[-1]:
      if is_palindrome(s):
        if p > largest:
          largest=p
print largest