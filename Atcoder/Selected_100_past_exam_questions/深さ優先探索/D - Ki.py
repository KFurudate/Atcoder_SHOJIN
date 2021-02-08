#https://atcoder.jp/contests/abc138/tasks/abc138_d
import sys
sys.setrecursionlimit(1000000)

n, q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n-1)]
PX = [list(map(int, input().split())) for _ in range(q)]

def dfs(v, p = -1):
    for u in to[v]:
        if u == p: continue
        ans[u] += ans[v]
        dfs(u, v)

to = [list() for _ in range(n+1)]
for a, b in AB:
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

ans = [0]*(n+1)
for p, x in PX:
    p -= 1
    ans[p] += x

dfs(0)
for i in range(n):
    print(ans[i])
