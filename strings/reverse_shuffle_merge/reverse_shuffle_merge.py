#!/usr/bin/env python

def capable(d1,d2):
  for key in d1.keys():
    if not d2.has_key(key) or d1[key] > d2[key]
      return False
  return True

def main(s):
  count = {}
  for c in s:
    if count.has_key(c):
      count[c] += 1
    else:
      count[c] = 1
  
  A_count = { key:count[key]/2 for key in count.keys() }
  i = 0
  f
  while A_count:
    count_ = copy(count)
    remain = sorted(A_count.keys(),reverse=True)
    for c in remain:
      for j in range(i,len(s)):
        
        if s[j] == c
    
