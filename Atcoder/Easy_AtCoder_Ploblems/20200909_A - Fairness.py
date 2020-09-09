a, b, c, k = map(int, input().split())

if k % 2:
    ans = b - a
else:
    ans = a - b

if abs(ans) > 10**18:
    print("Unfair")
else:
    print(ans)