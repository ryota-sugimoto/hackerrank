#!/usr/bin/env python

def main(s):
  for i in range(len(s)/2):
    if s[i] != s[-i-1]:
      if s[i+1:len(s)/2+1] == s[-i-1:len(s)/2:-1]:
        return i
      else:
        return len(s)-i-1
  return -1

import sys
T = int(sys.stdin.next())
for _ in range(T):
  print main(sys.stdin.next().strip())
