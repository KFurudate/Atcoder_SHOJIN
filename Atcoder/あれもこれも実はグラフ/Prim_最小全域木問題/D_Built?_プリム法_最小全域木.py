#https://atcoder.jp/contests/abc065/tasks/arc076_b

from heapq import *
import sys
input = sys.stdin.readline

def prim_heap():
    used = [False] * n
    e_lst = []
    for e in edge[0]:
        heappush(e_lst, e)
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

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

edge = [[] for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        w = min(abs(A[i][0] - A[j][0]), abs(A[i][1] - A[j][1]))
        edge[i].append((w, j))
        edge[j].append((w, i))

print(prim_heap())
###############
from heapq import *
from itertools import *
import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

def prim_heap():
    used = [False] * (10 ** 5)
    e_lst = []
    for e in edge[0]:
        heappush(e_lst, e)
    used[0] = True
    res = 0
    while e_lst:
        e_min = heappop(e_lst)
        v = e_min[1] - 1
        if used[v]: continue
        used[v] = True
        for e in edge[v]:
            if not used[e[1] - 1]:
                heappush(e_lst, e)
        res += e_min[0]
    return res

C = list(combinations(A, 2))
T = list(combinations(range(1, n + 1), 2))
W = [min(abs(c[0][0] - c[1][0]), abs(c[0][1] - c[1][1])) for c in C]

edge = [[] for _ in range(n + 1)]
for t, w in zip(T, W):
    edge[t[0]].append((w, t[1]))
    edge[t[1]].append((w, t[0]))

del edge[0]
print(prim_heap())

#########
def main():
    from heapq import *
    from itertools import *
    import sys
    input = sys.stdin.readline
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    def prim_heap():
        used = [False] * (10 ** 5)
        e_lst = []
        for e in edge[0]:
            heappush(e_lst, e)
        used[0] = True
        res = 0
        while e_lst:
            e_min = heappop(e_lst)
            v = e_min[1] - 1
            if used[v]: continue
            used[v] = True
            for e in edge[v]:
                if not used[e[1] - 1]:
                    heappush(e_lst, e)
            res += e_min[0]
        return res

    C = list(combinations(A, 2))
    T = list(combinations(range(1, n + 1), 2))
    W = [min(abs(c[0][0] - c[1][0]), abs(c[0][1] - c[1][1])) for c in C]
    w_list = nsmallest(n, W)
    edge = [[] for _ in range(n + 1)]
    for t, w in zip(T, W):
        if w in w_list:
            edge[t[0]].append((w, t[1]))
            edge[t[1]].append((w, t[0]))

    del edge[0]
    print(prim_heap())
if __name__ == '__main__':
    main()