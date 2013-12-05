#!/usr/bin/env python

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

current=40
keep_going=True
while keep_going:
  found=True
  for i in xrange(21,1,-1):
    if current % i != 0:
      found=False
      break
  if found:
    print current
    break
  current+=20