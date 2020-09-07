"""
n, max_w = map(int, input().split())

w = []
v = []
for i in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
"""

n=3
max_w =8
w =[3, 4, 5]
v =[30, 50, 60]

f_inf = float('inf')
max_v = 100000

dp = [f_inf]*(max_v+2)
dp[0] = 0

for i in range(1, n+1):
    for j in range(max_v+1, -1, -1):
        if j >= v[i-1]:
            dp[j] = min(dp[j], dp[j-v[i-1]]+w[i-1])

ans = 0
for i in range(max_v+1):
    if dp[i] <= max_w:
        ans = max(ans, i)
print(ans)