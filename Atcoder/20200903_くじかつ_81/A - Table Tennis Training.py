n, a, b = map(int, input().split())

ans = min(n-b, n-a)
if (b-a)%2:
    print(ans)
else:
    print(min(ans, (b-a)//2))
