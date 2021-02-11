n = int(input())
A = list(map(int, input().split()))

a0 = A[0]
cnt = 1
ans = 0
for a in A[1:]:
    if a <= a0:
        cnt += 1
    else:
        ans = max(ans, a0 * cnt)
        cnt = 1
    a0 = a

print(ans)

######################
#PyPy3:AC (Python3:TLE)
n = int(input())
A = list(map(int, input().split()))

ans = 0
for l in range(n):
    x = A[l]
    for r in range(l, n):
        x = min(x, A[r])
        ans = max(ans, x*(r-l+1))
print(ans)
