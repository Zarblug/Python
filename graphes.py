def adj(S,A):
  d = {}
  for s in S:
    d[s] = []
  for a in A:
    d[a[0]].append(a[1])
    d[a[1]].append(a[0])
  return d

def sommet(dic):
  d0= {}
  for s in dic.keys():
    d0[s]=len(adj[s])
  return d0

def mat_adj(S,l):
  M = [[0 for _ in range(len(S))] for _ in range(len(S))]
  for a in A:
    M[a[0]]M[a[1]] = 1
  return M

def sommets(d):
  T = []
  for i in d.keys:
    T.append(:)
  return T

from queue import Queue
