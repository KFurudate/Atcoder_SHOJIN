n, k = map(int, input().split())
H = sorted([int(input()) for _ in range(n)])

ans = 10 ** 9 + 1
for i in range(n - k + 1):
    tmp = H[k + i - 1] - H[i]
    ans = min(tmp, ans)

print(ans)
