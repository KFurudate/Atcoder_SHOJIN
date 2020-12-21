# TLE
n = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        print(A[i]-A[j])
        ans += abs(A[i]-A[j])
print(ans)

####################

# 累積和
n = int(input())
A = list(map(int, input().split()))
for i in range(1, n+1):
    cnt = abs(A[0]-A[i])