#!/usr/bin/env python

import string
from math import factorial

def main(s):
  d = { c: i for i,c in enumerate(string.lowercase) }
  l = [ d[c] for c in s ]
  count = {}
  for i in range(len(l)):
    c_count = [0] * len(string.lowercase)
    for j in range(i,len(l)):
      c_count[l[j]] += 1
      if count.has_key(tuple(c_count)):
        count[tuple(c_count)] += 1
      else:
        count[tuple(c_count)] = 1
  res = 0
  for key in count.keys():
    if count[key] > 1:
      res += factorial(count[key])/(factorial(2)*factorial(count[key]-2))
  return res

import sys
T = int(sys.stdin.next())
for _ in range(T):
  print main(sys.stdin.next().strip())
