n = int(input())
k = int(input())

AB = [list(map(int, input().split())) for _ in range(k)]

for a, b in AB:
    ans = min(a-1, n-a, b-1, n-b)
    ans %= 3
    ans += 1
    print(ans)
