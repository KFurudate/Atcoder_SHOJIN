n, m, c = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
for _ in range(n):
    A = list(map(int, input().split()))
    cnt = c
    for i in range(m):
        cnt += A[i] * B[i]
    if cnt > 0:
        ans += 1

print(ans)