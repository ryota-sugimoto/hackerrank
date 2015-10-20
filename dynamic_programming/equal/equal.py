#!/usr/bin/env python

def main(l):
  l.sort()
  res = 0
  diff_sum = 0
  last_diff = 0
  for i,x in enumerate(l[:-1]):
    next_x  = diff_sum + l[i+1]
    x = diff_sum - last_diff + x
    diff = next_x - x
    five_times = int(diff/5)
    five_remain = diff%5
    if five_remain == 3 or five_remain == 4:
      a = 2
    elif five_remain == 1 or five_remain == 2:
      a = 1
    else:
      a = 0
    res += a + five_times
    diff_sum += diff
    last_diff = diff
  return res

import sys
T = int(sys.stdin.next())
for _ in range(T):
  N = int(sys.stdin.next())
  l = map(int,sys.stdin.next().split())
  l2 = [l[0]] + [i+2 for i in l[1:]]
  l3 = [l[0]] + [i+1 for i in l[1:]]
  print min(main(l), main(l2)+1, main(l3)+1)
