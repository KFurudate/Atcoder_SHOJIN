n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

dp = [[ 0 for _ in range(3)]for _ in range(n+10)]

for i in range(3):
    dp[0][i] = A[0][i]

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][k] = max(dp[i][k], dp[i-1][j]+A[i][k])

print(max(dp[n-1]))
