n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
CD = [list(map(int, input().split())) for _ in range(k)]

k2 = 1 << k
ans = 0
for s in range(k2):
    dish = [0]*(n+1)
    for i in range(k):
        c, d = CD[i][0], CD[i][1]
        if (s >> i) & 1:
            dish[d] += 1
        else:
            dish[c] += 1

    now = 0
    for i in range(m):
        a, b = AB[i][0], AB[i][1]
        if dish[a] == 0: continue
        if dish[b] == 0: continue
        now += 1

    ans = max(ans, now)

print(ans)
