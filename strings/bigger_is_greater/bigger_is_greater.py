#!/usr/bin/env python
def swap(l,i):
  minimum = float("inf")
  swap_index = None
  for j in range(i+1,len(l)):
    if l[j] > l[i] and l[j] < minimum:
      swap_index = j
      minimum = l[j]
  return swap_index

import sys
import string
d = { c: i for i,c in enumerate(string.lowercase) }

T = int(sys.stdin.next())
for _ in range(T):
  s = sys.stdin.next().strip()
  l = [ d[c] for c in s ]
  for i in range(len(s)-1,-1,-1):
    swap_index = swap(l,i)
    if swap_index:
      l[i],l[swap_index] = l[swap_index],l[i]
      break
  if swap_index:
    l = l[0:i+1] + sorted(l[i+1:])
    print "".join(string.lowercase[i] for i in l)
  else:
    print "no answer"
