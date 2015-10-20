#!/usr/bin/env python

from string import lowercase
def main(s):
  d = { c:i for i,c in enumerate(lowercase) }
  l = [ d[c] for c in s ]
  res = 0
  for i in range(int(len(s)/2)):
    res += abs(l[i]-l[-i-1])
  return res

import sys
T = int(sys.stdin.next())
for _ in range(T):
  print main(sys.stdin.next().strip())
