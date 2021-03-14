n = int(input())
S = [input() for _ in range(5)]
f_inf = float("inf")

dp = [[f_inf]*3 for _ in range(n+1)]
color = ["R", "B", "W"]

for i in range(3):
    dp[0][i] = 0

for i in range(n):
    for j in range(3):
        cnt = 0
        for k in range(5):
            if S[k][i] == color[j]: continue
            cnt += 1

        min_cnt = f_inf
        for l in range(3):
            if j == l: continue
            min_cnt = min(min_cnt, dp[i][l])
        dp[i+1][j] = min_cnt + cnt

print(min(dp[-1]))
