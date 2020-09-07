#https://atcoder.jp/contests/abc120/tasks/abc120_d
#Thanks for this submission: https://atcoder.jp/contests/abc120/submissions/10531572

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
ilands = []
for _ in range(m):
    a, b = map(int, input().split())
    ilands.append((a-1, b-1))
rev_ilands = list(reversed(ilands))

uf = UnionFind(n)
ans = [0] * m
#Number of bridges connecting N islands
ans[m-1] = n*(n-1)//2

for i in range(m-1):
    if uf.find(rev_ilands[i][0]) != uf.find(rev_ilands[i][1]):
      n_bridgs= uf.size(rev_ilands[i][0])*uf.size(rev_ilands[i][1])
      ans[m-2-i] = ans[m-1-i] - n_bridgs
      uf.unite(rev_ilands[i][0], rev_ilands[i][1])
    else:
      ans[m-2-i] = ans[m-1-i]

for i in range(m):
    print(ans[i])