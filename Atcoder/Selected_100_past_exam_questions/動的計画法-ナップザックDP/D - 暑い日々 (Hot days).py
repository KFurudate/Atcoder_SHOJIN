n, d = map(int, input().split())
T = [int(input()) for _ in range(d)]
ABC = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(d)]
for i in range(n):
    a = ABC[i][0]
    b = ABC[i][1]
    c = ABC[i][2]
    t = T[0]
    if a <= t and t <= b:
        dp[0][i] = c
ans = 0
for i in range(1, d):
    t = T[i]
    for j in range(n):
        a = ABC[j][0]
        b = ABC[j][1]
        c = ABC[j][2]
        if a <= t and t <= b:
            for k in range(n):
                if dp[i - 1][k] == 0: continue
                if i == 1:
                    dp[i][j] = max(abs(c - ABC[k][2]), dp[i][j])
                    continue

                dp[i][j] = max(dp[i - 1][k] + abs(c - ABC[k][2]), dp[i][j])

print(max(dp[-1]))

