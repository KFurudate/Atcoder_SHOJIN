import sys
sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())

root = [-1] * n

def find(x):
    if root[x] < 0:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def unit(x, y):
    gx = find(x)
    gy = find(y)

    if gx == gy:
        return

    if root[gx] > root[gy]:
        gx, gy = gy, gx

    root[gx] += root[gy]
    root[gy] = gx



