import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
mod = 10**9+7

def comb(n, r):
    if 2*r > n: comb(n, n-r)
    return fac[n] * inv[r] * inv[n-r] % mod

def dfs(v, Pa=-1):
    for u in to[v]:
        if u == Pa: continue
        dfs(u, v)
        size[v] += size[u]
        dp[v] *= dp[u] % mod
        dp[v] *= comb(size[v], size[u]) % mod
    size[v] += 1

def bfs(v, Pa=-1, P_val=1, P_sz=0):
    ans[v] = P_val * dp[v] * comb(n-1, P_sz) % mod
    for u in to[v]:
        if u == Pa: continue
        x = dp[u] * comb(n-1, size[u])
        val = ans[v] * pow(x, mod-2, mod) % mod
        bfs(u, v, val, n-size[u])

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

n = 8
to = [[1], [0, 2], [1, 3, 4, 5], [2], [2], [2, 6, 7], [5], [5]]


fac = [1] * (n+1)
inv = [1] * (n+1)

for i in range(2, n+1):
    fac[i] = fac[i-1] * i % mod
inv[n] = pow(fac[n], mod-2, mod)
for i in range(n-1, 1, -1):
    inv[i] = inv[i+1] * (i+1) % mod

dp = [1] * n
size = [0] * n
ans = [0] * n

dfs(0)
bfs(0)
print(*ans, sep='\n')