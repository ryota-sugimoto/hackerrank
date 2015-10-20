#!/usr/bin/env python

def distance(bikers, bikes):
  res = []
  for i, (biker_x, biker_y) in enumerate(bikers):
    for j, (bike_x, bike_y) in enumerate(bikes):
      res.append(((i,j),(biker_x-bike_x)**2 + (biker_y-biker_y)**2))
  res.sort(reverse=True,key = lambda ((i,j),d): d)
  return res

def req_time(distance,K):
  used_biker = set([])
  used_bike = set([])
  while K:
    (biker, bike), d = distance.pop()
    if biker in used_biker or bike in used_bike:
      pass
    else:
      used_biker.add(biker)
      used_bike.add(bike)
      res = d
      K -= 1
  return res

import sys
N,M,K = map(int, sys.stdin.next().split())
bikers = []
for i in range(N):
  bikers.append(tuple(map(int,sys.stdin.next().split())))
bikes = []
for i in range(M):
  bikes.append(tuple(map(int,sys.stdin.next().split())))

distances = distance(bikers,bikes)
print req_time(distances,K)
