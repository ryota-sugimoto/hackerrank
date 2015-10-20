#!/usr/bin/env python

def main(N,C):
  p = []
  for i in range(len(C)):
    p.append([1])
  for i in range(1,N+1):
    for j,c in enumerate(C):
      n = 0
      if c <= i:
        n += p[j][i-c]
      if j > 0:
        n += p[j-1][i]
      p[j].append(n)
  return p

import sys
N, M = map(int,sys.stdin.next().split())
C = map(int,sys.stdin.next().split())
print main(N, C)[M-1][N]
