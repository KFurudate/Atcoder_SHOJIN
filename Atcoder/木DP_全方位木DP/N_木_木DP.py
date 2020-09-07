#https://tdpc.contest.atcoder.jp/tasks/tdpc_tree

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

f_inf = float('inf')
mod = 10**9+7

def comb(x, y):
    if 2 * y > x: return comb(x, x-y)
    return fac[x] * inv[y] * inv[x-y] % mod

def dfs(v, root=-1):
    sz, dp = 0, 1
    SZ = []
    SZ_append = SZ.append
    for u in to[v]:
      if u == root: continue
      s, p = dfs(u, v)
      sz += s
      dp *= p % mod
      SZ_append(s)
    tmp = sz
    for s in SZ:
        dp *= comb(tmp, s) % mod
        tmp -= s
    return sz+1, dp

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
n = 4
to = [[1], [0, 2], [1, 3], [2]]

#前処理
fac = [1] * (n+1)
inv = [1] * (n+1)
for i in range(2, n+1):
    fac[i] = fac[i-1] * i % mod
inv[n] = pow(fac[n], mod-2, mod)
for i in range(n-1, 1, -1):
    inv[i] = inv[i+1] * (i+1) % mod

ans = 0
for i in range(n):
     ans += dfs(i)[1] % mod
print(ans * inv[2] % mod)

################
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

mod = 10 ** 9 + 7


def comb(x, y):
    if 2 * y > x: return comb(x, x - y)
    return fac[x] * inv[y] * inv[x - y] % mod


def dfs(v, root=-1):
    sz, dp = 0, 1
    for u in to[v]:
        if u == root: continue
        s, p = dfs(u, v)
        sz += s
        dp *= p
        dp *= comb(sz, s)
    return sz + 1, dp

n = int(input())
to = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

fac = [1] * (n + 2)
inv = [1] * (n + 2)
for i in range(2, n + 1):
    fac[i] = fac[i - 1] * i % mod
inv[n] = pow(fac[n], mod-2, mod)
for i in range(n - 1, 1, -1):
    inv[i] = inv[i + 1] * (i + 1) % mod

ans = 0
for i in range(n):
    ans += dfs(i)[1] % mod
print(ans * inv[2] % mod)