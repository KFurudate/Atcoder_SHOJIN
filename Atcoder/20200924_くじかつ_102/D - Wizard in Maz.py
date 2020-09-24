# 解説AC, 01-DFS
# Pypy3

from collections import deque
import sys
input = lambda :sys.stdin.readline().rstrip()

def INPUT(mode = int):
    return list(map(mode, input().split()))

h, w = INPUT()
Ch, Cw = INPUT()
Dh, Dw = INPUT()

Ch -= 1
Cw -= 1
Dh -= 1
Dw -= 1

S = [input() for _ in range(h)]

f_inf = float("inf")
dist = [[f_inf] * w for _ in range(h)]
dist[Ch][Cw] = 0

di = (-1, 0, 1, 0)
dj = (0, -1, 0, 1)

que = deque([])
que.append((Ch, Cw))

while que:
    p = que.popleft()
    i, j = p[0], p[1]
    d = dist[i][j]

    if dist[i][j] != d: continue;

    for idx in range(4):
        ni, nj = i+di[idx], j+dj[idx]

        if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
        if S[ni][nj] == "#": continue
        if dist[ni][nj] <= d: continue

        dist[ni][nj] = d
        que.appendleft((ni, nj))

    for ei in range(-2, 3):
        for ej in range(-2, 3):
            ni, nj = i+ei, j+ej

            if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
            if S[ni][nj] == "#": continue
            if dist[ni][nj] <= d+1: continue

            dist[ni][nj] = d+1
            que.append((ni, nj))

ans = dist[Dh][Dw]
if ans == f_inf: ans = -1
print(ans)
