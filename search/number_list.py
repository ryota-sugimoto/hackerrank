#!/usr/bin/env python

def greater_than_indexes(l, K):
  res = []
  for i,n in enumerate(l):
    if n > K:
      res.append(i)
  res.append(len(l))
  return res

def num_sub_array_from_index(indexes):
  res = 0
  last = indexes[0]
  for index in indexes[1:]:
    res += (last + 1) * (index - last)
    last = index
  return res

import sys

T = int(sys.stdin.next())
for i in range(T):
  N,K = map(int, sys.stdin.next().split())
  A = map(int, sys.stdin.next().split())
  indexes = greater_than_indexes(A,K)
  print num_sub_array_from_index(indexes)
