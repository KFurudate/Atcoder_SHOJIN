n, t = map(int, input().split())
A = [int(input()) for _ in range(n)]

tmp = A[0] + t
cnt = t
for a in A[1:]:
    if a > tmp:
        cnt += t
    else:
        cnt += a + t - tmp
    tmp = a + t
print(cnt)