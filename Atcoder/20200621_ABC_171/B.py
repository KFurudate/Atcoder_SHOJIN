n, k = map(int, input().split())
P = sorted(list(map(int, input().split())))

ans = 0
for p in P[:k+1]:
    ans += p

print(ans)


