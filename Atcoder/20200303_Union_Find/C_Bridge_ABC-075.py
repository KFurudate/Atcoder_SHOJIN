# https://atcoder.jp/contests/abc075/tasks/abc075_c
# I used the below code as a reference.
# https://atcoder.jp/contests/abc075/submissions/10369947
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
        return [i for i in self._root if i < 0]

n, m = map(int, input().split())
nodes = []
for _ in range(m):
    a, b = map(int, input().split())
    nodes.append((a, b))

cnt = 0
for i in range(m):
    uf = UnionFind(n)
    for j in range(m):
        if i != j:
            uf.unite(nodes[j][0]-1, nodes[j][1]-1)
    cnt += (len(uf.roots()) != 1)
print(cnt)