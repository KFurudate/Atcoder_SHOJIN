n, k = map(int, input().split())
P = sorted(list(map(int, input().split())))

ans = sum(P[:k])
print(ans)