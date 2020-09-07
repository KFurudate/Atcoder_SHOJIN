n = int(input())

g = [[] for _ in range(n)]

for i in range(n):
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split())
        g[i].append((x-1, y))

ans = 0

for i in range(1, 2 ** n):
    ok = True
    for j in range(n):
        if (i >> j) & 1 == 0:
            continue
        for x, y in g[j]:
            if (i >> x)& 1 != y:
                ok = False
                break
        if not ok:
            break
    if ok:
        ans = max(ans, bin(i)[2:].count('1'))
print(ans)
