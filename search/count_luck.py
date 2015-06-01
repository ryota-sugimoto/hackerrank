#!/usr/bin/env python

def count_luck(mat, i, j):
  mat = [ ["X"] + s + ["X"] for s in mat ]
  n = len(mat[0])
  mat = [["X"]*n] + mat
  mat.append(["X"]*n)
  i += 1
  j += 1
  directions = [(-1,0),
                (1,0),
                (0,1),
                (0,-1)]
  def move(i, j, K):
    if mat[i][j] == "*":
      return K
    mat[i][j] = "X"
    d = []
    for di,dj in directions:
      if mat[i+di][j+dj] != "X":
        d.append((di,dj))
    if not d:
      return -float("inf")
    elif len(d) == 1:
      return move(i+d[0][0], j+d[0][1], K)
    else:
      res = []
      for di, dj in d:
        res.append(move(i+di, j+dj, K+1))
      return max(res)

  return move(i, j, 0)

import sys
T = int(sys.stdin.next())
for t in range(T):
  N, M = map(int, sys.stdin.next().split())
  mat = []
  for i in range(N):
    l = list(sys.stdin.next().strip())
    if "M" in l:
      M_i, M_j = i, l.index("M")
    mat.append(l)
  K = int(sys.stdin.next())
  if K == count_luck(mat, M_i, M_j):
    print "Impressed"
  else:
    print "Oops!"
