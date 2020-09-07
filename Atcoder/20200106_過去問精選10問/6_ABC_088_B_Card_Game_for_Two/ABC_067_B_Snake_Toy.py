N, K = map(int, input().split())
l = list(map(int, input().split()))

L = sorted(l, reverse=True)

ans = 0
for k in range(K):
    ans += L[k]

print(ans)
