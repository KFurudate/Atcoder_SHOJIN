n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n-k+1):
    T = A[i:i+k]
    tmp = T[0]
    for t in T[1:]:
        if tmp >= t: break
        tmp = t
    else:
      cnt += 1

print(cnt)

#################################

n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]

cnt = 1
ans = 0
tmp = A[0]
for a in A[1:]:
     diff = a - tmp
     tmp = a
     cnt += 1
     if diff <= 0:
         cnt = 0
     if cnt >= k-1:
         ans += 1
print(ans)

####################################
#数列の数を数える
n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]

cnt = 0
ans = 0
tmp = 0
for a in A:
    if a > tmp:
        cnt += 1
    else:
        cnt = 1
    tmp = a
    if cnt >= k:
        ans += 1
print(ans)