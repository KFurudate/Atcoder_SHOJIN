"""
n, k = 4, 3
to = [[1], [0, 2], [1, 3], [2]]
MOD = 10**9+7
"""

import sys
sys.setrecursionlimit(10**7)

n, k = map(int, input().split())
to = [list() for _ in range(n)]
MOD = 10**9+7

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

cnt = [0] * n
def dfs(v, p=-1):
    if p == -1:
        n_cnt = 1
    else:
        n_cnt = 2
    for u in to[v]:
        if u == p:
            continue
        cnt[u] = n_cnt
        n_cnt += 1
        dfs(u, v)
    return cnt

ans = 1
for i in dfs(0):
  ans *= max(0, k-i)
  ans %= MOD

print(ans)