#https://atcoder.jp/contests/atc001/tasks/unionfind_a
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
        if gx == gy:
            return False
        if self._root[gx] > self._root[gy]:
            gx, gy = gy, gx
        self._root[gx] += self._root[gy]
        self._root[gy] = gx
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -(self._root[self.find(x)])

n, q = map(int, input().split())
uf = UnionFind(n)

for _ in range(q):
    p, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if p == 0:
        uf.unite(a, b)
    else:
        if uf.same(a, b) == True:
            print('Yes')
        else:
            print('No')