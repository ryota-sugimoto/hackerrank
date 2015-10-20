#!/usr/bin/env python

def main(A,B):
  if len(A) != len(B):
    return -1
  A_n = len(filter(lambda c: c == "1",A))
  B_n = len(filter(lambda c: c == "1",B))
  if A_n != B_n:
    return -1
  
  return len(filter(lambda (c1,c2): c1=="0" and c2=="1", zip(A,B)))

import sys
A=sys.stdin.next().strip()
B=sys.stdin.next().strip()
print main(A,B)
