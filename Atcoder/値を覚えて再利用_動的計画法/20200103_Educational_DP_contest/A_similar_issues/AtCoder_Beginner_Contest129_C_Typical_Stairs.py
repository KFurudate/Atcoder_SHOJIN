n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]

mod = 1000000007
brok = [False] * (n+1)

for i in a:
    brok[i] = True

dp = [0] * (n+2)
dp[n] = 1

for i in range(n-1, -1, -1):
    if brok[i]:
        dp[i] = 0
        continue
    else:
        dp[i] = (dp[i+1]+dp[i+2]) % mod

print(dp[0])