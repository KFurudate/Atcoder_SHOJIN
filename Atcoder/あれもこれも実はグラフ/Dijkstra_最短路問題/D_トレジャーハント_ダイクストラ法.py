#https://atcoder.jp/contests/abc035/tasks/abc035_d
#高速化

import heapq
import sys

input = sys.stdin.readline

def Dijkstra_heap(s, edge):
    # 始点sから各頂点への最短距離#始点sから各頂点への最短距離
    d = [10**20] * n
    used = [False] * n
    d[s] = 0
    used[s] = True
    edgelist = []
    for i, j in edge[s]:
        heapq.heappush(edgelist, i+j*(10**6))
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        v = minedge % (10**6)
        # まだ使われてない頂点の中から最小の距離のものを探す
        if used[v]: continue
        d[v] = minedge // (10**6)
        used[v] = True
        for e in edge[v]:
            if not used[e[0]]:
                heapq.heappush(edgelist, e[0]+(e[1]+d[v]) * (10**6))
    return d

n, m, t = map(int, input().split())
edge = [[] for _ in range(n)]
edge2 = [[] for _ in range(n)]
A = list(map(int, input().split()))
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, c))
    edge2[b].append((a, c))

# 頂点iまでの最短距離
dist1 = Dijkstra_heap(0, edge)
# 頂点iからの最短距離
dist2 = Dijkstra_heap(0, edge2)

ans = 0
for i in range(n):
    ans = max(ans, (t - (dist1[i] + dist2[i])) * A[i])
print(ans)