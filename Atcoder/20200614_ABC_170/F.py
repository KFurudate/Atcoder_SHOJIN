from collections import deque
import sys
input = sys.stdin.readline

h, w, k = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1-=1
y1-=1
x2-=1
y2-=1

dist = [input() for _ in range(h)]
ans = [[-1]*w for _ in range(h)]
ans[x1][y1] = 0

que = deque()
que.append((x1, y1))
direction = ((1, 0), (-1, 0), (0, -1), (0, 1))
while que:
  x, y = que.popleft()

  if x == x2 and y == y2:
      print(ans[x][y])
      exit()

  for dx, dy in direction:
    for i in range(1, k+1):
      kx = x + dx*i
      ky = y + dy*i

      if not(0 <= kx < h and 0 <= ky < w) or dist[kx][ky] == "@":
          break

      if 0 <= ans[kx][ky] <= ans[x][y]:
          break

      if ans[kx][ky] == -1:
          que.append((kx, ky))

      ans[kx][ky] = ans[x][y]+1

print(-1)