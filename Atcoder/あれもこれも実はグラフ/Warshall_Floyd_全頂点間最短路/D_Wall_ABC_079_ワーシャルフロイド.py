#https://atcoder.jp/contests/abc079/tasks/abc079_d

import sys
input = sys.stdin.readline

def Warshall_Floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d
h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
n = 10
Warshall_Floyd(c)

A = [list(map(int, input().split())) for _ in range(h)]
S = []
S_append = S.append
for a in A:
    for i in a:
      if i != -1 and i != 1:
        S_append(i)
ans = 0
for s in S:
  ans += c[s][1]
print(ans)