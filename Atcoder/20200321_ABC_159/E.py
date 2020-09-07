#bit 貪欲法
#二次元マトリックスinput

def add(j):
    for i in range(g):
        now[i] += c[i][j]
    for i in range(g):
        if now[i] > k: return False
    return True

import sys
input = lambda: sys.stdin.readline().rstrip()

f_inf = float('inf')
c = [[0] * 10 for _ in range(1005)]

"""
h, w, k = map(int, input().split())
S = [[int(i) for i in input()] for _ in range(h)]h, w, k = map(int, input().split())
S = [[int(i) for i in input()] for _ in range(h)]
"""

h, w, k = 3, 5, 4
S = [[1, 1, 1, 0, 0], [1, 0, 0, 0, 1], [0, 0, 1, 1, 1]]
ans = f_inf
for div in range(1<<(h-1)):
    g = 0 #g: the number of group
    id = [0] * h
    for i in range(h):
        id[i] = g
        if (div>>i) & 1:
            g += 1
    g += 1

    for i in range(g):
        for j in range(w):
            c[i][j] = 0
    for i in range(h):
        for j in range(w):
            c[id[i]][j] += S[i][j]
    ok = True
    for i in range(g):
        for j in range(w):
            if c[i][j] > k:
                ok = False
    if not ok: continue

    num = g - 1
    now = [0] * g
    for j in range(w):
        if not add(j):
            num += 1
            now = [0] * g
            add(j)
    ans = min(ans, num)
print(ans)