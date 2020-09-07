#https://atcoder.jp/contests/abc073/tasks/abc073_d

import sys
import itertools

input = sys.stdin.readline

def Washall_Floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d

n, m, r = map(int, input().split())
R = list(map(int, input().split()))
f_inf = float('inf')
dist = [[f_inf]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = c
    dist[b][a] = c

Washall_Floyd(dist)

S = list(itertools.permutations(R, r))
cnt = f_inf
for s in S:
  tmp = 0
  for i in range(len(s)-1):
    tmp += dist[s[i]-1][s[i+1]-1]
  cnt = min(cnt, tmp)
print(cnt)

