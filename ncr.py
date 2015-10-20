#!/usr/bin/env python

from math import factorial
def gen_ncr():
  d = {}
  def ncr(n,r):
    if d.has_key((n,r)):
      print "hit"
      return d[(n,r)]
    else:
      d[(n,r)] = factorial(n)/(factorial(r)*factorial(n-r))
      return d[(n,r)]
  return ncr

ncr = gen_ncr()
print ncr(10,2)
print ncr(10,2)
