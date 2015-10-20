#!/usr/bin/env python

def main(l,k):
  l = sorted(list(set(l)))
  p = []
  for i in range(k+1):
    if i < l[0]:
      p.append(0)
    else:
      p.append(max(x+p[i-x] for x in l if x <= i))
  return p[-1]

import sys
T = int(sys.stdin.next())
for _ in range(T):
  n,k = map(int,sys.stdin.next().split())
  l = map(int,sys.stdin.next().split())
  print main(l,k)
