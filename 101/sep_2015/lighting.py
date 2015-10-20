#!/usr/bin/env python

def tree(l,N):
  res = [ {"link": []} for _ in range(N) ]
  for i,j in l:
    res[i]["link"].append(j)
    res[j]["link"].append(i)
  return res

def light(t,l):
  for i,light in enumerate(l):
    t[i]["light"] = light
  return t

def main(t):
  stack = [(t[0],None)]
  res = 0
  while stack:
    node,parent = stack[-1]
    if len(node["link"]) == 1 and parent:
      node["solved"] = True
      stack.pop()
    else:
      all_solved = True
      all_lighted = True
      for child in [ t[i] for i in node["link"] if t[i] is not parent]:
        if not child.has_key("solved"):
          stack.append((child,node))
          all_solved = False
          break
        elif not child["light"]:
          all_lighted = False
      if all_solved:
        if not all_lighted and not node["light"]:
          res += 1
          node["light"] = 1
        node["solved"] = True
        stack.pop()
  return res


import sys
T = int(sys.stdin.next())
for _ in range(T):
  N = int(sys.stdin.next())
  lig = map(int,sys.stdin.next().split())
  l = []
  for __ in range(N-1):
    l.append(tuple(map(lambda c: int(c)-1,sys.stdin.next().split())))
  t = tree(l,N)
  light(t,lig)
  print main(t)
