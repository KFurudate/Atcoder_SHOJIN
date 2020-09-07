#https://atcoder.jp/contests/abc012/tasks/abc012_4

import sys
input = sys.stdin.readline

def Washall_Floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

n, m = map(int, input().split())
f_inf = float('inf')
dist = [[f_inf] * n for _ in range(n)]
for i in range(n): dist[i][i] = 0

for _ in range(m):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = t
    dist[b][a] = t

Washall_Floyd(dist)
print(min(max(d) for d in dist))
