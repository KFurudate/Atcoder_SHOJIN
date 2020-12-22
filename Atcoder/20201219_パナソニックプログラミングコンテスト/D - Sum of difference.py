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

n = int(input())
A = sorted(list(map(int, input().split())))

s = 0
ans = 0
for i in range(n):
    ans += A[i]*i
    ans -= s
    s += A[i]

print(ans)
