from collections import deque
import sys
input = sys.stdin.readline
f_inf = float('inf')
def push(v, d):
    if dist[v] != f_inf: return
    dist[v] = d
    que.append(v)

#n, x, y = map(int, input().split())
n, x, y = 5, 2, 4
x -= 1
y -= 1

ans = [0] * n
for sv in range(n):
    dist = [f_inf] * n
    que = deque([])
    push(sv, 0)

    while que:
        v = que.popleft()
        d = dist[v] + 1
        if v - 1 >= 0: push(v - 1, d)
        if v + 1 < n: push(v + 1, d)
        if v == x: push(y, d)
        if v == y: push(x, d)

    for i in range(n):
        ans[dist[i]] += 1

for i in range(n):
    ans[i] = ans[i] // 2

for i in range(1, n):
    print(ans[i])