#!/usr/bin/env python

def main(r):
  N = len(r)
  r = [float("inf")] + r + [float("inf")]
  c = [0]*(N+2)
  def solve(i):
    if (r[i-1] >= r[i]) and (r[i] <= r[i+1]):
      c[i] = 1
    else:
      n = []
      if r[i-1] < r[i]:
        if c[i-1] == 0:
          solve(i-1)
        n.append(c[i-1]+1)
      if r[i+1] < r[i]:
        if c[i+1] == 0:
          solve(i+1)
        n.append(c[i+1]+1)
      c[i] = max(n)
  for i in range(1,N+1):
    solve(i)
  return sum(c)

import sys
N = int(sys.stdin.next())
r = [int(l) for l in sys.stdin]
print main(r)
