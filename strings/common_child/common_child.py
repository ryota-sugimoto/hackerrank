#!/usr/bin/env python

def main(s1,s2):
  p1 = [0]*(len(s2)+1)
  p2 = [0]*(len(s2)+1)
  for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
      c1,c2 = s1[i-1],s2[j-1]
      if c1 == c2:
        p1[j] = p2[j-1] + 1
      else:
        p1[j] = max(p1[j-1],p2[j])
    p1,p2 = p2,p1
  return p2[-1]

import sys
s1 = sys.stdin.next().strip()
s2 = sys.stdin.next().strip()
print main(s1,s2)
