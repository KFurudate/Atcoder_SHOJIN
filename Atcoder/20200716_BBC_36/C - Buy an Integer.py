import math

A, B, X = map(int, input().split())

if A >= B:
    n = math.ceil(X / A)
else:
    n = math.ceil(X / B)

cnt = 0
for i in range(n + 1):
    n -= i
    tmp = A*n + (B*len(str(n)))
    if tmp <= X:
        cnt = max(cnt, tmp)
        ans = n

print(ans)

########################
A, B, X = map(int, input().split())

def calc(n):
    return A*n + B*len(str(n))

#初期状態
l = 0
r = 10**9+1

#二分探索
while (l+1 < r):
    mid = (l+r)//2
    if calc(mid) <= X:
        l = mid
    else:
        r = mid
    #print(l, r)

print(l)
