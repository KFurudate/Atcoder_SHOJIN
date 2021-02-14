from collections import deque

def bfs(sx, sy, gx, gy):
    f_inf = float('inf')
    dist = [[f_inf] * w for _ in range(h)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que = deque([])
    que.append((sx, sy))
    dist[sx][sy] = 0

    while que:
        p = que.popleft()

        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if h > nx >= 0 and w > ny >= 0 and \
                    maze[nx][ny] != 'X' and \
                    dist[nx][ny] == f_inf:
                que.append((nx, ny))
                dist[nx][ny] = dist[p[0]][p[1]] + 1

    return dist[gx][gy]

h, w, n = map(int, input().split())
maze = [input() for _ in range(h)]

goals = []
for idx_h, row in enumerate(maze):
    for idx_w, area in enumerate(row):
        if "S" in area:
            sy, sx = idx_w, idx_h
        elif (area != ".") and (area != "X"):
            goals.append((int(area), idx_w, idx_h))

ans = 0
goals = sorted(goals)
for cheese, gy_, gx_ in goals:
    ans += bfs(sx, sy, gx_, gy_)
    sx, sy = gx_, gy_

print(ans)