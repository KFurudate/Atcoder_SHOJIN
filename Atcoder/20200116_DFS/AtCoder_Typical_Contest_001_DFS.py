from collections import deque

def dfs(sx, sy, gx, gy):
    dist = [[f_inf] * w for _ in range(h)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    stack = deque([])
    stack_append = stack.append
    stack_append((sx, sy))
    dist[sx][sy] = 0

    while stack:
        p = stack.pop()
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if h > nx >= 0 and w > ny >= 0 and \
               c[nx][ny] != '#' and \
               dist[nx][ny] == f_inf:
                stack_append((nx, ny))
                dist[nx][ny] = dist[p[0]][p[1]] + 1
    return dist[gx][gy]

h, w = map(int, input().split())
c = [input() for _ in range(h)]
f_inf = float('inf')

for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            sx, sy = i, j
        elif c[i][j] == 'g':
            gx, gy = i, j

if dfs(sx, sy, gx, gy) == f_inf:
    print('No')
else:
    print('Yes')