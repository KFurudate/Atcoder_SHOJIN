# https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d

n, m = map(int, input().split())
D = [0] + [int(input()) for _ in range(n)]
C = [0] + [int(input()) for _ in range(m)]

f_inf = float("inf")

dp = [[f_inf] * (m + 1) for _ in range(n + 1)]
for i in range(m + 1):
    dp[0][i] = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = min(dp[i-1][j-1] + (D[i] * C[j]), dp[i][j-1])
print(dp[-1][-1])

