a, b, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = min(A) + min(B)

for _ in range(m):
    x, y, c = map(int, input().split())
    cnt = A[x] + B[y] - c
    ans = min(ans, cnt)

print(ans)