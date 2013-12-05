#!/usr/bin/env python

# returns set of natural numbers less
# than 'less_than' and a multiple of the values in 'multiples_of'
# e.g. less_than=10 and multiple_of=[3,5] would return [0, 3, 5, 6, 9]
def natural_numbers_multiple(less_than=0, multiples_of=[]):
  return set([x for x in xrange(0,less_than) for m in multiples_of if x % m == 0])

multiples = natural_numbers_multiple(less_than=1000, multiples_of=[3,5]);
print sum(multiples)