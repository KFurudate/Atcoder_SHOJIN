n = int(input())
h = list(map(int, input().split()))

dp = [1] * n
dp[0] = 0

for i in range(1, n):
    if i == 1:
        dp[i] = abs(h[i] - h[i-1])
    else:
        dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))

print(dp[n-1])