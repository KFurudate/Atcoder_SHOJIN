class UnionFind():
    def __init__(self, N):
        self._root = [-1 for i in range(N)]

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
nodes = []
for _ in range(m):
    u, v = map(int, input().split())
    nodes.append((u - 1, v - 1))

uf1 = UnionFind(n)
for node1 in nodes:
    uf1.unite(node1[0], node1[1])

roots = []
children = []
for i, x in enumerate(uf1.roots()):
    if x < 0:
        roots.append(i)
    else:
        children.append((x, i))

cnt = 0
for root in roots:
    tree = []
    tree.append(root)
    if len(roots) != len(uf1.roots()):
        for child in children:
            if root == child[0]:
                tree.append(child[1])
            else:
                continue

    for node1 in nodes:
        uf2 = UnionFind(n)
        node1 = tuple(set(node1) & set(tree))
        if not node1: continue

        for node2 in nodes:
            node2 = tuple(set(node2) & set(tree))
            if not node2: continue

            if node1 != node2:
                uf2.unite(node2[0], node2[1])

        if uf2.same(node1[0], node1[1]):
            cnt += 1
            break

        else:
            continue

print(len(roots) - cnt)