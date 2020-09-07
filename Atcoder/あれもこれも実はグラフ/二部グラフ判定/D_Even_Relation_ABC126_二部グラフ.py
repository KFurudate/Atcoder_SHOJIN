#https://atcoder.jp/contests/abc126/tasks/abc126_d
#n = 5
#g = [[(2, 8)], [(4, 2), (2, 10)], [(1, 10), (0, 8), (3, 2)], [(2, 2)], [(1, 2)]]

import sys
sys.setrecursionlimit(10 ** 7)

def dfs(v, p, c):
    color[v] = c
    for vi, wi in g[v]:
        if vi == p: continue
        if wi % 2: dfs(vi, v, 1-c)
        else: dfs(vi, v, c)
    return color

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, w))
    g[v].append((u, w))

color = [0 for _ in range(n)]
for i in dfs(0, -1, 0):
    print(i)