n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]
edges = [[] for _ in range(n)]
for a, b in AB:
    edges[a - 1].append(b)
    edges[b - 1].append(a)
print(edges)

cnt = 0
ans = [-1] * n
for idx, edge in enumerate(edges):
    ans[idx] = 0
    for e in set(edge):
        if ans[e - 1] == -1:
            cnt += 1
            ans[e - 1] = 0
            print(ans, cnt)

print(cnt)
##############
#WA
n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]
edges = [[] for _ in range(n)]
for a, b in AB:
    edges[a - 1].append(b)
    edges[b - 1].append(a)
print(edges)

ans = 0
print(edges)
for edge in edges:
    ans = max(ans, len(set(edge)+1))

print(ans)

########################
n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]
edges = [[] for _ in range(n)]
for a, b in AB:
    edges[a - 1].append(b)
    edges[b - 1].append(a)

ans = 0
for edge in edges:
    print(len(set(edge)))
    ans = max(ans, len(set(edge))+1)

print(ans)
############################
# Union find
# かっつぱさんの解説と公式のスライドみた
# https://www.youtube.com/watch?time_continue=916&v=zxor0DdwoXA&feature=emb_logo
# https://www.slideshare.net/chokudai/union-find-49066733
# ユニオン
import sys

sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]

root = [-1] * n


def find(x):
    if root[x] < 0:
        return x
    else:
        root[x] = find(root[x])
        return root[x]


def unite(x, y):
    gx = find(x)
    gy = find(y)

    if gx == gy:
        return

    if root[gx] > root[gy]:
        gx, gy = gy, gx

    root[gx] += root[gy]
    root[gy] = gx


def size(x):
    x = find(x)
    return -root[x]


for a, b in AB:
    a -= 1
    b -= 1
    unite(a, b)

ans = 0
for i in range(n):
    ans = max(ans, size(i))
print(ans)

