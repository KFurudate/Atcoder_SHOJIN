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