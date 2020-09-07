from collections import deque
import sys

input = sys.stdin.readline

f_inf = float("inf")

n, m = map(int, input().split())
to = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

que = deque([])
que.append(0)

dist = [f_inf for _ in range(n)]
dist[0] = 0

guide = [-1 for _ in range(n)]

while que:
    v = que.popleft()
    for u in to[v]:
        if dist[u] != f_inf: continue
        dist[u] = dist[v] + 1
        guide[u] = v
        que.append(u)

print("Yes")
for i in range(1, n):
    ans = guide[i] + 1
    print(ans)
