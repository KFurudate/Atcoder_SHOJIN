from collections import deque

def bfs():
    dist = [[f_inf] * w for _ in range(h)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que = deque([])
    que.append((0, 0))
    dist[0][0] = 0

    while que:
        p = que.popleft()
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if h > nx >= 0 and w > ny >= 0 and \
               C[nx][ny] != '#' and \
               dist[nx][ny] == f_inf:
                que.append((nx, ny))
                dist[nx][ny] = dist[p[0]][p[1]]+1
    return dist[h-1][w-1]

h, w = map(int, input().split())
C =[input() for _ in range(h)]
f_inf = float('inf')

cnt = 0
for c in C:
    cnt += c.count('.')

if bfs() == f_inf:
    print(-1)
else:
    print(cnt - 1 - bfs())

