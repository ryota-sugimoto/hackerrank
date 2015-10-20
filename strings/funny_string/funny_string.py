#!/usr/bin/env python

def main(S):
  N = len(S)
  R = "".join(reversed(list(S)))
  for i in range(1,N):
    if abs(ord(S[i])-ord(S[i-1])) != abs(ord(R[i])-ord(R[i-1])):
      return False
  return True

import sys
T = int(sys.stdin.next())
for _ in range(T):
  print "Funny" if main(sys.stdin.next().strip()) else "Not Funny"

