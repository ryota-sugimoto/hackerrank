#!/usr/bin/env python

def grid_search(G,P):
  R = len(G)
  C = len(G[0])
  r = len(P)
  c = len(P[0])
  p = P[0]
  for i in range(R-r+1):
    g = G[i]
    poss = []
    pos = -1
    while True:
      pos = g.find(p,pos+1)
      if pos > -1:
        poss.append(pos)
      else:
        break
    for pos in poss:
      P_i = 1
      for G_i in range(i+1,i+r):
        gg = G[G_i][pos:pos+c]
        if P[P_i] != gg:
          break
        P_i += 1
        if P_i == r:
          return True
  return False

import sys
T = int(sys.stdin.next())
for i in range(T):
  R,C = map(int,sys.stdin.next().split())
  G = []
  for j in range(R):
    G.append(sys.stdin.next().strip())
  r,c = map(int,sys.stdin.next().split())
  P = []
  for j in range(r):
    P.append(sys.stdin.next().strip())
  print "YES" if grid_search(G,P) else "NO"
      
