#WA
#P=R=Sのときダメ
n, k = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

ans = [0] * n
for i in range(n):
    if T[i] == "r":
        ans[i] = P
    if T[i] == "s":
        ans[i] = R
    if T[i] == "p":
        ans[i] = S

for i in range(n - k):
    if ans[i] == ans[i + k]:
        ans[i + k] = 0
print(sum(ans))
########################
#AC
n, k = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

for i in range(n-k):
    if T[i] == T[i+k]:
        T[i+k] = ""

ans = 0
for i in range(n):
    if T[i] == "r":
        ans += P
    if T[i] == "s":
        ans += R
    if T[i] == "p":
        ans += S

print(ans)

# 解説AC
# DP

# dp[i][j] = iターン目までやったとき、最後に勝った/負けたor引き分け
# j = 0, 1

