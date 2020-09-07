s = input()
t = input()

s_len = len(s)
t_len = len(t)

dp = [[0 for _ in range(t_len + 1)] for _ in range(s_len + 1)]

for i in range(1, s_len + 1):
    for j in range(1, t_len + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

ans = ''
x = s_len
y = t_len

while x > 0 and y > 0:
    if dp[x][y] == dp[x - 1][y]:
        x -= 1
    elif dp[x][y] == dp[x][y - 1]:
        y -= 1
    else:
        x -= 1
        y -= 1
        ans = ans + s[x]

ans = ans[::-1]
print(ans)



