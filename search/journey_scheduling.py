#!/usr/bin/env python

class tree:
  def __init__(self, l):
    N = len(l) + 1
    m = []
    for i in range(N):
      m.append({"nearest": []})
    for i, j in l:
      m[i]["nearest"].append(j)
      m[j]["nearest"].append(i)
  
    self.t = []
    for i in range(N):
      self.t.append({"children":[]})
    self.t[0]["parent"] = -1
    stack = [(0,-1)]
    while stack:
      n,p = stack.pop()
      if m[n]["nearest"] == [p]:
        self.t[n]["children"] = []
      else:
        for near_node in m[n]["nearest"]:
          if near_node != p:
            self.t[n]["children"].append(near_node)
            self.t[near_node]["parent"] = n
            stack.append((near_node,n))

  def add_height(self):
    stack = [0]
    while stack:
      n = stack[-1]
      if not self.t[n]["children"]:
        self.t[n]["height"] = 0
        stack.pop()
      else:
        height = 0
        f = True
        for child in self.t[n]["children"]:
          if not self.t[child].has_key("height"):
            stack.append(child)
            f = False
          else:
            h = self.t[child]["height"]
            if h > height: height = h
        if f: 
          self.t[n]["height"] = height + 1
          stack.pop()
           
  def add_high(self):
    stack = [0]
    while stack:
      n = stack.pop()
      if n == 0:
        self.t[n]["high"] = 0
      if not self.t[n]["children"]:
        pass
      elif len(self.t[n]["children"]) == 1:
        child = self.t[n]["children"][0]
        self.t[child]["high"] = self.t[n]["high"]+1
        stack.append(child)
      else:
        heights = [(child,self.t[child]["height"]) \
                   for child in self.t[n]["children"]]
        heights.sort(key = lambda (fst,snd): snd)
        highest_child, highest_height = heights.pop()
        snd_highest_child, snd_highest_height = heights.pop()
        for child in self.t[n]["children"]:
          l = []
          if child == highest_child:
            l.append(snd_highest_height+2)
          else:
            l.append(highest_height+2)
          l.append(self.t[n]["high"]+1)
          self.t[child]["high"] = max(l)
          stack.append(child)
        
    
  def max_distance(self):
    l = []
    def farthest(n):
      if len(self.t[n]["children"]) > 1:
        m = []
        for child in self.t[n]["children"]:
          m.append(self.t[child]["height"])
        m.sort()
        snd,fst = m[-2:]
        l.append(fst+snd+2)
    for i in range(len(self.t)):
      farthest(i)
    return max(l)
  
  def farthest_distance(self,n):
    l = []
    for child in self.t[n]["children"]:
      l.append(self.t[child]["height"]+1)
    l.append(self.t[n]["high"])
    return max(l)

import sys
N,M = map(int, sys.stdin.next().split())
l = []
for i in range(N-1):
  l.append(map(lambda s: int(s)-1 , sys.stdin.next().split()))
t = tree(l)
t.add_height()
t.add_high()
max_d = t.max_distance()
for s in sys.stdin:
  V,K = map(int, s.split())
  first_travel_distance = t.farthest_distance(V-1)
  print first_travel_distance + max_d * (K-1)
  
