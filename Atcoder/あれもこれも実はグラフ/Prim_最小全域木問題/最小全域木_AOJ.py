#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A&lang=jp

from heapq import *
def prim_heap():
    used = [False] * n
    e_lst = []
    for e in edge[0]:
        heappush(e_lst,e)
    used[0] = True
    res = 0
    while e_lst:
        e_min = heappop(e_lst)
        v = e_min[1]
        if used[v]: continue
        used[v] = True
        for e in edge[v]:
            if not used[e[1]]:
                heappush(e_lst, e)
        res += e_min[0]
    return res

n, k = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(k):
    s, t, w = map(int, input().split())
    edge[s].append((w, t))
    edge[t].append((w, s))
print(prim_heap())
