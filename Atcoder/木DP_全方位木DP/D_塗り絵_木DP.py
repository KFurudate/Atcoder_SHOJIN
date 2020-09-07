#https://abc036.contest.atcoder.jp/tasks/abc036_d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

mod = 10**9+7

def dfs(v, root=-1):
    fx, gx = 1, 1
    for u in to[v]:
        if u == root: continue
        fy, gy = dfs(u, v)
        fx *= fy + gy
        gx *= fy
    return fx, gx

"""
n = int(input())
to = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)
"""
n = 5
#to = [[7], [4], [9], [7], [7, 1], [8, 7], [8], [0, 9, 5, 4, 3], [6, 5], [7, 2]]
to = [[4], [4, 3, 2], [1], [1], [1, 0]]

fx, gx = dfs(0)
print((fx+gx) % mod)