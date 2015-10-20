#!/usr/bin/env python

def main(l):
  maximum = l[-1]
  profits = []
  for i in range(len(l)-1, -1, -1):
    if l[i] > maximum:
      maximum = l[i]
    else:
      profits.append(maximum - l[i])
  return sum(profits)

import sys
T = int(sys.stdin.next())
for i in range(T):
  N = int(sys.stdin.next())
  l = map(int,sys.stdin.next().split())
  print main(l)
