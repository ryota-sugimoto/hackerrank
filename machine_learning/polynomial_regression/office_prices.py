#!/usr/bin/env python

from numpy import matrix

def calc_A(x,M):
  memo = [ sum(xx**i for xx in x) for i in range(M*2) ]
  l = [ [memo[i+j] for i in range(M)] for j in range(M) ]
  return matrix(l)

def calc_T(x,y,M):
  l = [[sum(xx**i*yy for (xx,yy) in zip(x,y))] for i in range(M)]
  return matrix(l)

def new_y(A,T,M,new_x):
  W = A**-1 * T
  l = [ new_x**i for i in range(M) ]
  return float(matrix(l).dot(W))

M = 3
import sys
F,N = map(int, sys.stdin.next().split())
X = []
for i in range(F):
  X.append([])
y = []
for i in range(N):
  t = map(float, sys.stdin.next().split())
  for j in range(F):
    X[j].append(t[j])
  y.append(t[-1])

T = int(sys.stdin.next())
test_x = []
for l in sys.stdin:
  test_x.append(map(float,l.split()))

A_list = map(lambda x: calc_A(x,M), X)
T_list = map(lambda x: calc_T(x,y,M), X)

W_list = [ A**-1 * T for A,T in zip(A_list,T_list) ]

for x_list in test_x:
  print [new_y(A,T,M,new_x) for A,T,new_x in zip(A_list,T_list,x_list)]

