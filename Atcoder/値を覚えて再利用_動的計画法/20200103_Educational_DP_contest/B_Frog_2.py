n, k = map(int, input().split())
h = list(map(int, input().split()))

def chmin(a, b):
    if a > b:
        return b
    else:
        return a

f_inf = float('inf')

for _ in range(k+2):
    h.append(f_inf)

dp = [f_inf]*(n+k)

dp[0] = 0

for i in range(1, n):
    for j in range(1, k+1):
        if i >= j:
            dp[i] = chmin(dp[i], dp[i-j] + abs(h[i] - h[i-j]))

print(dp[n-1])