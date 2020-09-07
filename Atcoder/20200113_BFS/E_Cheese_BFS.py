from collections import deque

def bfs(sx, sy, gx, gy):
    f_inf = float('inf')
    dist = [[f_inf]* w for _ in range(h)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que = deque([])
    que.append((sx, sy))
    dist[sx][sy] = 0

    while que:
        p = que.popleft()
        if p[0] == gx and p[1] == gy:
            break

        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if h > nx >= 0 and w > ny >= 0 and\
               c[nx][ny] != 'X' and \
               dist[nx][ny] == f_inf:
                que.append((nx, ny))
                dist[nx][ny] = dist[p[0]][p[1]]+1

    return dist[gx][gy]

h, w, n = map(int, input().split())
c = [input() for _ in range(h)]


cheeze = ['S']
for i in range(1, n+1):
    cheeze.append(str(i))

s_to_g = []
for k in cheeze:
    for i in range(h):
        for j in range(w):
            if c[i][j] == k:
                s_to_g.append((i, j))
cnt = 0
for i in range(n):
    j = i + 1
    sx, sy = s_to_g[i]
    gx, gy = s_to_g[j]
    cnt += bfs(sx, sy, gx, gy)

print(cnt)

h, w, n =10, 10, 9
c =['.X...X.S.X',
    '6..5X..X1X',
    '...XXXX..X',
    'X..9X...X.',
    '8.X2X..X3X',
    '...XX.X4..',
    'XX....7X..',
    'X..X..XX..',
    'X...X.XX..',
    '..X.......']
