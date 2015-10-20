#!/usr/bin/env python

def n_ways(x, d, M):
  memo = {}
  def loop(x,M):
    if memo.has_key((x,M)):
      return memo[(x,M)]

    if M == 0:
      return 1

    if x == d and x == 1:
      return 0

    if x == 1:
      memo[(x,M)] = loop(x+1, M-1)
    elif x == d:
      memo[(x,M)] = loop(x-1, M-1) 
    else:
      memo[(x,M)] = loop(x-1, M-1) + loop(x+1, M-1)
    return memo[(x,M)]
    
  return loop(x,M)


from math import factorial
def gen_ncr():
  d = {}
  def ncr(n,r):
    if d.has_key((n,r)):
      return d[(n,r)]
    else:
      d[(n,r)] = factorial(n)/(factorial(r)*factorial(n-r))
      return d[(n,r)]
  return ncr

def main(x, D, M):
  N = len(D)
  n_way_memo = {}
  for i,(xi,di) in enumerate(zip(x,D)):
    for k in range(M+1):
      n_way_memo[(i,k)] = n_ways(xi,di,k)
  print "memo done"

  ncr = gen_ncr()

  memo = {}
  def loop(i, n):
    if n == 0:
      return 1
    if i == N-1:
      return n_way_memo[(i,n)]
    if memo.has_key((i,n)):
      return memo[(i,n)]
    
    l = []
    for k in range(n+1):
      l.append(ncr(n,k) * n_way_memo[(i,k)] * loop(i+1,n-k))
    memo[(i,n)] = sum(l)
    return memo[(i,n)]
  return loop(0,M)

import sys
T = int(sys.stdin.next())
for i in range(T):
  N,M = map(int,sys.stdin.next().split())
  x = map(int,sys.stdin.next().split())
  D = map(int,sys.stdin.next().split())
  print main(x,D,M)%1000000007
