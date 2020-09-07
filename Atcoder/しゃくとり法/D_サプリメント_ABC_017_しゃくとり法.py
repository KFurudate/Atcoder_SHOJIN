#https://atcoder.jp/contests/abc017/tasks/abc017_4
#n, m = map(int, input().split())
#F = [int(input()) for _ in range(n)]

n, m = 5,  2
F = [1, 2, 1, 2, 2]

#しゃくとり法
fnum = [0]*(m+1) #区間に種類 i が何個あるか
L = [0]*(n+1)    #各 i に対するしゃくとり法の区間
l = 0
for r in range(n):
    fnum[F[r]] += 1
    while l < r and fnum[F[r]] > 1:
        fnum[F[l]] -= 1
        l += 1
    L[r+1] = l

#累積和で高速化した DP
f_inf = float('inf')
dp = [f_inf]*100010
dp[0] = 1

S = [0]*100010
S[1] = 1
MOD = 10**9+7

for i in range(1, n+1):
    dp[i] = (S[i]-S[L[i]]+MOD) % MOD
    S[i+1] = (S[i]+dp[i]) % MOD

print(dp[n])