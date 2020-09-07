#https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_d

from heapq import heappush, heappop
import sys

input = sys.stdin.readline


def Dijkstra_heap(s, edge):
    d = [10 ** 20] * n
    used = [False] * n
    d[s] = 0
    used[s] = True
    edgelst = []
    for i, j in edge[s]:
        heappush(edgelst, i + j * (10 ** 6))
    while edgelst:
        edgemin = heappop(edgelst)
        v = edgemin % (10 ** 6)
        if used[v]: continue
        d[v] = edgemin // (10 ** 6)
        used[v] = True
        for e in edge[v]:
            if not used[e[0]]:
                heappush(edgelst, e[0] + (e[1] * (10 ** 6)))

    return d


n, m, s, t = map(int, input().split())
yen = [[] for _ in range(n)]
snk = [[] for _ in range(n)]
for _ in range(m):
    u, v, a, b = map(int, input().split())
    yen[u - 1].append((v - 1, a))
    yen[v - 1].append((u - 1, b))
    snk[u - 1].append((v - 1, a))
    snk[v - 1].append((u - 1, b))

cos1 = Dijkstra_heap(s-1, yen)
cos2 = Dijkstra_heap(t-1, snk)

for i in range(n):
