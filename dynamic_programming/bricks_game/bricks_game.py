#!/usr/bin/env python

def main(l):
  l.reverse()
  p = []
  sum_score = 0
  for i,x in enumerate(l):
    sum_score += x
    if i < 3:
      p.append(sum_score)
    else:
      score = max(sum_score-p[i-j-1] for j in range(3))
      p.append(score)
  return p[-1]

import sys
T = int(sys.stdin.next())
for _ in range(T):
  N = int(sys.stdin.next())
  l = map(int,sys.stdin.next().split())
  print main(l)
