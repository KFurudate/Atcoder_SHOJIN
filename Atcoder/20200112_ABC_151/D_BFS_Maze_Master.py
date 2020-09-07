from collections import deque

#Start(sx, sy)から各頂点への最短距離を求める

def bfs(sx, sy):
    cnt = 0
    f_inf = float('inf')
    dist = [[f_inf] * m for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    #Start地点を0にする
    que = deque([])
    que.append((sx, sy))
    dist[sx][sy] = 0

    while que:
        p = que.popleft()

        for i in range(4):
            #移動した点を(nx, ny)とする
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            #移動可能かと既に訪れたかの判定
            #dist[nx][ny] != f_infなら既に訪れた
            if n > nx >= 0 and \
               m > ny >= 0 and \
               s[nx][ny] != '#' and \
               dist[nx][ny] == f_inf:
                que.append((nx, ny))
                dist[nx][ny] = dist[p[0]][p[1]] + 1
                cnt = dist[nx][ny]

    return cnt


n, m = map(int, input().split())
s = [input() for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if s[i][j] == '#':
            continue
        ans = max(ans, bfs(i, j))
print(ans)

#n = 3
#m = 5
#s =['...#.', '.#.#.', '.#...']




