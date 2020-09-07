n = int(input())
h = [int(i) for i in input().split()]

#dpの最小値を変更する関数
def chmin(a, b):
    if a > b:
        return b
    else:
        return a

f_inf = float('inf')

#DPテーブルの初期化
dp = [f_inf] * (10**5+10)

#初期条件
dp[0] = 0

for i in range(1, n):
    dp[i] = chmin(dp[i], dp[i-1]+ abs(h[i]-h[i-1]))

    if i > 1:
        dp[i] = chmin(dp[i], dp[i-2] + abs(h[i]-h[i-2]))
print(dp[n-1])