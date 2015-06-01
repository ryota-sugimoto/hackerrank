#!/usr/bin/env python

def left(l):
  l = [float("inf")] + l
  res = [0] * len(l)
  for i in range(1,len(l)):
    if l[i-1] > l[i]:
      res[i] = i-1
    else:
      j = i-1
      while l[res[j]] <= l[i]:
        j = res[j]
      res[i] = res[j]
  return res[1:]

def right(l):
  l = l + [float("inf")]
  res = [0]*len(l)
  for i in range(len(l)-2,-1,-1):
    if l[i+1] > l[i]:
      res[i] = i+1
    else:
      j = i+1
      while l[res[j]] <= l[i]:
        j = res[j]
      res[i] = res[j]
  return [i+1 if i != len(l)-1 else 0 for i in res[:-1]]

import sys
N = int(sys.stdin.next())
a = map(int, sys.stdin.next().split())

l = left(a)
r = right(a)

#print a
#print l
#print r

print max(i*j for i,j in zip(l,r))
