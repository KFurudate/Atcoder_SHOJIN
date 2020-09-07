#https://atcoder.jp/contests/dp/tasks/dp_p

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

mod = 10**9+7

def dfs(v, Pa=-1):
    white, black = 1, 1
    for u in to[v]:
        if u == Pa: continue
        x, y = dfs(u, v)
        white *= x+y
        black *= x
    return white, black

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
n = 10
to = [[4, 6], [9, 8], [5], [7], [7, 5, 0], [4, 2], [0], [4, 9, 3], [1], [7, 1]]

white, black = dfs(0)
print((white+black) % mod)