#https://atcoder.jp/contests/arc097/tasks/arc097_b
class UnionFind():
    def __init__(self, N):
        self._root = [-1 for _ in range(N)]

    def find(self, x):
        if self._root[x] < 0: return x
        self._root[x] = self.find(self._root[x])
        return self._root[x]

    def unite(self, x, y):
        gx = self.find(x)
        gy = self.find(y)
        if gx == gy: return False
        if self._root[gx] > self._root[gy]:
            gx, gy = gy, gx
        self._root[gx] += self._root[gy]
        self._root[gy] = gx
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -(self._root[self.find(x)])

    def roots(self):
        return [i for i in self._root]


n, m = map(int, input().split())
P = list(map(int, input().split()))
par = []
for _ in range(m):
    x, y = map(int, input().split())
    par.append((x - 1, y - 1))

uf = UnionFind(n)
for i in range(m):
    uf.unite(par[i][0], par[i][1])

cnt = 0
for i in range(n):
  if uf.same(i, P[i]-1):
    cnt += 1
print(cnt)