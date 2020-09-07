#https://atcoder.jp/contests/abc158/tasks/abc158_f

from heapq import *
import sys

input = sys.stdin.readline


def comb(n, r):
    if 2 * r > n: return comb(n, n - r)
    return fac[n] * inv[r] * inv[n - r] % mod


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
    return sz + 1, dp


mod = 998244353

# input
n = int(input())
P = sorted([tuple(map(int, input().split())) for _ in range(n)])
Hq = []
for p in P:
    heappush(Hq, (-p[0], p[1]))

to = [[] for i_ in range(n * 10)]
for i in range(n - 1, 0, -1):
    x, d = P[i][0], P[i][1]
    s = heappop(Hq)
    heappush(Hq, s)
    while Hq and -s[0] < x + d:
        to[i].append(s[1])
        s = heappop(Hq)
    heappush(Hq, (-x, i))

fac = [1] * (n * 10)
inv = [1] * (n * 10)
for i in range(2, n + 1):
    fac[i] = fac[i - 1] * i % mod
inv[n] = pow(fac[n], mod - 2, mod)
for i in range(n - 1, 1, -1):
    inv[i] = inv[i + 1] * (i + 1) % mod

ans = 0
for i in range(n):
    ans += dfs(i)[1] % mod
    print(ans)
print(ans)