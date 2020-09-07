#Union Find union find

#Root: -1
#child: Parent's ID(non-negative)


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


n, m, k = map(int, input().split())
uf = UnionFind(n)
cnt = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    cnt[a] += 1
    cnt[b] += 1
    uf.unite(a, b)

for _ in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if uf.same(a, b) == True:
      cnt[a] += 1
      cnt[b] += 1

for i in range(n):
    ans = (uf.size(i) - 1) - cnt[i]
    print(ans, end=" ")