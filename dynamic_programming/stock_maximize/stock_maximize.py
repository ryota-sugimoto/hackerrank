#!/usr/bin/env python

def main(l):
  N = len(l)
  last_day_price = l[-1]
  p = []
  for i in range(N):
    p.append(last_day_price*i)

  for i in range(1,N):
    day = N - i - 1
    price = l[day]
    pp = []
    pp.append(max(p[0], p[1] - price))
    for n_stock in range(1,day+1):
      pp.append(max(pp[n_stock-1]+price, p[n_stock+1]-price))
    p = pp
  return p[-1]

import sys
T = int(sys.stdin.next())
for i in range(T):
  N = int(sys.stdin.next())
  l = map(int,sys.stdin.next().split())
  print main(l)
