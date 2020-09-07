#BFS木
#queue
from collections import deque
import sys
input = sys.stdin.readline

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

f_inf = float("inf")
dist = [f_inf for _ in range(n)]
dist[0] = 0

pre = [-1 for _ in range(n)]

while que:
    #queの先頭から頂点を取り出す
    v = que.popleft()
    #その頂点の辺ををたどって隣接する頂点をみる
    for u in to[v]:
        #もし、隣接する頂点の距離がわかっている場合は何もしない
        if dist[u] != f_inf: continue
        #隣接する頂点の距離を直前の頂点（v）+1で更新する
        dist[u] = dist[v] + 1
        #直前の頂点(v)をメモする
        pre[u] = v
        que.append(u)

print("Yes")
for i in range(n):
    if i == 0: continue
    ans = pre[i]
    ans += 1
    print(ans)