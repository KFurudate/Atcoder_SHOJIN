n=3
max_w =8
w =[3, 4, 5]
v =[30, 50, 60]

"""
n, max_w = map(int, input().split())

w = []
v = []
for i in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
"""


dp = [[0 for _ in range(max_w+1)] for _ in range(n+2)]

for i in range(1, n+1):
    for j in range(max_w+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j >= w[i-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-w[i-1]]+v[i-1])

print(max(dp[n]))