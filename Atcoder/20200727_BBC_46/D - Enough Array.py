#TLE
from itertools import accumulate

n, k = map(int, input().split())
A = list(map(int, input().split()))
S = [0] + list(accumulate(A))
#print(S)


cnt = 0

for i in range(n, -1, -1):
    for j in range(i+1):
        #print(i, j)
        if i != j:
            if S[i]-S[j] >= k:
                cnt += 1
                #print(i, j)
print(cnt)

###############################
# 解説放送
# 方針：全パターン数からk未満のものを引く
# 尺取り（しゃくとり）

n, k = map(int, input().split())
A = list(map(int, input().split()))

Right = 0
Scope = 0
ans = 0

for Left in range(n):
    while (Right < n) & (Scope + A[Right]) < k:
        Scope += A[Right]
        Right += 1

    ans += Right - Left
    Scope -= A[Right]

#全パターン数: n*(n+1)/2
ans = n*(n+1)/2 - ans
print(ans)

###############################

# 累積和 + bisect
# https://at274.hatenablog.com/entry/2018/01/12/090000

from itertools import accumulate

n, k = map(int, input().split())
A = list(map(int, input().split()))
S = [0] + list(accumulate(A))
#print(S)

