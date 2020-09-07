n, m = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(m)]

for x in range(1000):
    keta = 1
    nx = x // 10
    d = [x % 10]

    while nx:
        keta += 1
        d.append(nx % 10)
        nx //= 10
    d.reverse()
    if keta != n:
        continue

    ok = True
    for i in range(m):
        if d[p[i][0] - 1] != p[i][1]:
            ok = False
    if ok:
        print(x)
        exit()

print(-1)