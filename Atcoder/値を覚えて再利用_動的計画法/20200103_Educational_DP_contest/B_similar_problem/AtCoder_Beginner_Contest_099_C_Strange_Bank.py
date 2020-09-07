n = int(input())
MAXN = 110000

f_inf = float('inf')
dp = [f_inf] * (MAXN+n)

dp[0] = 0

for i in range(1, n+2):
    for j in range(7):
        dp[i] = min(dp[i], dp[i-pow(6, j)]+1)
    for k in range(6):
        dp[i] = min(dp[i], dp[i-pow(9, k)]+1)

print(dp[n])