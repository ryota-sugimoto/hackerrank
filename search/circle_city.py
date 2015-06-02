#!/usr/bin/env python

from math import sqrt

def is_y_int(sq_r, sq_x):
  sq_y = sq_r - sq_x
  min_y = int(sqrt(sq_y))
  return min_y**2 == sq_y

import sys
t = int(sys.stdin.next())
for s in sys.stdin:
  sq_r, k = map(int,s.split())
  r = sqrt(sq_r)
  max_x = int(r)
  n = 0
  for x in range(max_x):
    if is_y_int(sq_r, x**2):
      n += 1
  n *= 4
  print "possible" if k >= n else "impossible"
