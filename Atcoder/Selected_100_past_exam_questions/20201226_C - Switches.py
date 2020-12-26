# https://atcoder.jp/contests/abc128/tasks/abc128_c

n, m = map(int, input().split())
KS = [list(map(int, input().split())) for _ in range(m)]
P = list(map(int, input().split()))

ans = 0
for i in range(2 ** n):
    cnt = 0
    Bit = [0] * m
    for j in range(m):
        for s in KS[j][1:]:
            s -= 1
            if (i >> s) & 1:
                Bit[j] += 1
        if Bit[j] % 2 == P[j]:
            cnt += 1
    #print(Bit, i, cnt)
    if cnt == m:
        ans += 1
print(ans)
