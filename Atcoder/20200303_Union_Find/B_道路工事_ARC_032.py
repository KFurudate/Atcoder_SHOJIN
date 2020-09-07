#https://arc032.contest.atcoder.jp/tasks/arc032_2

class UnionFind():
    def __init__(self, N):
        self._root = [-1 for _ in range(N)]

    def find(self, x):
        if self._root[x] < 0: return x
        return self._root[x] = self.find(self._root[x])

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

    def g_num(self):
        cnt = 0
        for i in range(len(self._root)):
            if self._root[i] < 0:
                cnt += 1
        return cnt

n, m = map(int, input().split())
uf = UnionFind(n)

for _ in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  uf.unite(a, b)

print(uf.g_num()-1)