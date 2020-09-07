#https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f
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
        heappush(edgelst, i+j*(10**6))
    while edgelst:
        edgemin = heappop(edgelst)
        v = edgemin % (10**6)
        if used[v]: continue
        d[v] = edgemin // (10**6)
        used[v] = True
        for e in edge[v]:
            if not used[e[0]]:
                heappush(edgelst, e[0]+(e[1]+d[v])*(10**6))
    return d

n, m, s, t = map(int, input().split())
Yen = [[] for _ in range(n)]
Snk = [[] for _ in range(n)]

for _ in range(m):
    u, v, a, b = map(int, input().split())
    u, v = u-1, v-1
    Yen[u].append((v, a))
    Yen[v].append((u, a))
    Snk[u].append((v, b))
    Snk[v].append((u, b))

cos1 = Dijkstra_heap(s-1, Yen)
cos2 = Dijkstra_heap(t-1, Snk)

ans = 0
ANS = []
ANS_append = ANS.append
for yen,snk in zip(cos1[::-1], cos2[::-1]):
  tmp = 10**15-(yen+snk)
  ans = max(ans, tmp)
  ANS_append(ans)
print(*ANS[::-1], sep='\n')