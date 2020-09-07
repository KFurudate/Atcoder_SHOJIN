import sys
input=lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**8)

class LCA(object):
    def __init__(self, to, root=0):
        self.__n = len(to)
        self.__to = to
        self.__logn = (self.__n - 1).bit_length()
        self.__depth = [-1] * self.__n
        self.__dist = [-1] * self.__n
        self.__depth[root] = 0
        self.__dist[root] = 0
        self.__parents = [[-1] * self.__n for _ in range(self.__logn)]
        self.__dfs(root)
        self.__doubling()

    def __dfs(self, v):
        for u in self.__to[v]:
            if self.__depth[u] != -1: continue
            self.__parents[0][u] = v
            self.__depth[u] = self.__depth[v] + 1
            self.__dfs(u)

    def __doubling(self):
        for i in range(1, self.__logn):
            for v in range(self.__n):
                if self.__parents[i - 1][v] == -1: continue
                self.__parents[i][v] = self.__parents[i-1][self.__parents[i-1][v]]

    @property
    def depth(self):
        return self.__depth

    @property
    def dist(self):
        return self.__dist

    def get(self, u, v):
        dd = self.__depth[v] - self.__depth[u]
        if dd < 0:
            u, v = v, u
            dd *= -1
        for i in range(self.__logn):
            if dd & (2 ** i):
                v = self.__parents[i][v]
        if v == u: return v
        for i in range(self.__logn - 1, -1, -1):
            pu = self.__parents[i][u]
            pv = self.__parents[i][v]
            if pu != pv: u, v = pu, pv
        return self.__parents[0][u]

def resolve():
    n = int(input())
    to = [[] for _ in range(n)]
    for _ in range(n-1):
        x, y = map(int, input().split())
        x -= 1; y -= 1
        to[x].append(y)
        to[y].append(x)

    G = LCA(to)
    q = int(input())
    ans = []
    ans_append = ans.append
    for _ in range(q):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        ans_append((a, b))
    for i in ans:
        print(G.depth[i[0]] + G.depth[i[1]] \
              -2*(G.depth[G.get(i[0], i[1])])+1)
resolve()