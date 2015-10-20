#!/usr/bin/env python

def main(s1,s2):
  s1 = s1 + "a"
  s2 = s2 + "a"
  res = []
  i,j = 0,0
  while i < len(s1) or j < len(s2):
    if i < len(s1) and j < len(s2):
      c1 = s1[i]
      c2 = s2[j]
      if c1 == c2:
        if s1[i:] < s2[j:]:
          res.append(c1)
          i += 1
        else:
          res.append(c2)
          j += 1
      elif c1 < c2:
        res.append(c1)
        i += 1
      else:
        res.append(c2)
        j += 1
    elif i < len(s1):
      res.append(s1[i])
      i += 1
    else:
      res.append(s2[j])
      j += 1
  return "".join(res)[:-2]

import sys
T = int(sys.stdin.next())
for _ in range(T):
  s1 = sys.stdin.next().strip()
  s2 = sys.stdin.next().strip()
  print main(s1,s2)
