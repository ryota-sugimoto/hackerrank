#!/usr/bin/env python

def max_mod(l,M):
  max_mod_here = max_so_far = 0
  for x in l:
    max_mod_here = max(x, (max_mod_here + x) % M)
    max_so_far = max(max_so_far , max_mod_here)
  return max_so_far

import sys
T = int(sys.stdin.next())
for i in range(T):
  N,M = map(int,sys.stdin.next().split())
  l = map(int,sys.stdin.next().split())
  l_mod = map(lambda x: x% M, l)
  print max_mod(l_mod,M)
