#!/usr/bin/env python

def n_ways(x, d, M):
  if d == 1:
    l = [1]
    for i in range(M):
      l.append(0)
    return l
  l = []
  l.append([1 if i == x else 0 for i in range(1,d+1)])
  for k in range(M):
    last = l[-1]
    m = []
    for x in range(d):
      if x == 0:
        m.append(last[1])
      elif x == d-1:
        m.append(last[-2])
      else:
        m.append(last[x-1] + last[x+1])
    l.append(m)
  return map(sum, l)

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
  n_way_memo = []
  for xi,di in zip(x,D):
    n_way_memo.append(n_ways(xi,di,M))

  ncr = gen_ncr()

  memo = {}
  def loop(i, n):
    if n == 0:
      return 1
    if i == N-1:
      return n_way_memo[i][n]
    if memo.has_key((i,n)):
      return memo[(i,n)]
    l = []
    for k in range(n+1):
      l.append(ncr(n,k) * n_way_memo[i][k] * loop(i+1,n-k))
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
