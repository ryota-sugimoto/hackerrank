#!/usr/bin/env python

from math import sqrt
def primes(n):
  if n < 2:
    return []
  l = range(2,n+1)
  x = l[0]
  res = []
  while x <= sqrt(n):
    x = l[0]
    l = filter(lambda i:i%x != 0,l)
    res.append(x)
  return res+l

def brick(N):
  l = [1]
  for i in range(1,N+1):
    if i < 4:
      l.append(1)
    else:
      l.append(l[-1] + l[-4])
  return l[-1]

import sys
T = int(sys.stdin.next())
for i in range(T):
  N = int(sys.stdin.next())
  print len(primes(brick(N)))
