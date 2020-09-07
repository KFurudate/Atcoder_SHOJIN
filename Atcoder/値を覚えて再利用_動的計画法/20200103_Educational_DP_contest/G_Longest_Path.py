from collections import deque
n, m = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n)]
out_deg = [0] * n
dp = [0]*n

for x, y in xy:
    graph[y-1].append(x-1)
    out_deg[x-1] += 1

stack = deque([i for i in range(n) if out_deg[i] == 0])

while stack:
    node = stack.popleft()
    for i in graph[node]:
        dp[i] = max(dp[i], dp[node]+1)
        out_deg[i] -= 1
        if out_deg[i] == 0:
            stack.append(i)

print(max(dp))