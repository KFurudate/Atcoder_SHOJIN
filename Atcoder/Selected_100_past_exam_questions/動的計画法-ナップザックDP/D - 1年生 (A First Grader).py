n = int(input())
lst = list(map(int, input()))

dp = [[0]*21 for _ in range(n+1)]
dp[0][lst[0]] = 1

for i in range(1, n):
    for j in range(21):
        if j + lst[i] <= 20:
            dp[i][j] += dp[i-1][j+lst[i]]
        else:
            dp[i][j] += dp[i-1][j-lst[i]]
        print(dp)

print(dp[n-2][lst[n-1]])