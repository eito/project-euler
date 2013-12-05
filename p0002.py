#!/usr/bin/env python

# returns list of fibonacci numbers less than 'less_than'
def fibonacci_generator(less_than=0):
  nums=[]
  a, b = 1, 2
  while a < less_than:
    nums.append(a)
    a,b = b,a+b
  return nums
  
s=0
for x in fibonacci_generator(4000000):
  if x % 2 == 0:
    s+=x
print s