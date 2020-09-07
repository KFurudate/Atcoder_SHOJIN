import sys
input=lambda :sys.stdin.readline().rstrip()

#n = int(input())
#A = list(map(int, input().split()))

n = 27
A = [18, -28, 18, 28, -45, 90, -45, 23, -53, 60, 28, -74, -71, 35, -26, -62, 49, -77, 57, 24, -70, -93, 69, -99, 59, 57, -49]

k = 1+n%2
f_inf = float('inf')

dp = [[-f_inf for _ in range(4)] for _ in range(200005)]
dp[0][0] = 0
for i in range(n):
    for j in range(k+1):
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])
        now = dp[i][j]
        if (i+j)%2 == 0: now += A[i]
        dp[i+1][j] = max(dp[i+1][j], now)

ans = dp[n][k]
print(ans)