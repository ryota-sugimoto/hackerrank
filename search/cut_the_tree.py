#!/usr/bin/env python

class tree:
  def __init__(self, l,V):
    N = len(l) + 1
    m = []
    for i in range(N):
      m.append({"nearest": []})
    for i, j in l:
      m[i]["nearest"].append(j)
      m[j]["nearest"].append(i)
  
    self.t = []
    for i in range(N):
      self.t.append({"children":[],"value": V[i]})
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

  def add_sub_tree_value(self):
    stack = [0]
    while stack:
      n = stack[-1]
      if not self.t[n]["children"]:
        self.t[n]["sub_tree_value"] = self.t[n]["value"]
        stack.pop()
      else:
        sum_value = 0
        f = True
        for child in self.t[n]["children"]:
          if not self.t[child].has_key("sub_tree_value"):
            stack.append(child)
            f = False
          elif f:
            sum_value += self.t[child]["sub_tree_value"]
        if f: 
          self.t[n]["sub_tree_value"] = sum_value + self.t[n]["value"]
          stack.pop()
           
import sys
N = int(sys.stdin.next())
V = map(int,sys.stdin.next().split())
l = []
for i in range(N-1):
  l.append(map(lambda s: int(s)-1 , sys.stdin.next().split()))
t = tree(l,V)
t.add_sub_tree_value()
print min(abs(2*n["sub_tree_value"]-t.t[0]["sub_tree_value"]) for n in t.t)
