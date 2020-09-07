n = int(input())
d, x = map(int, input().split())

ans = x
for _ in range(n):
    a = int(input())
    tmp = a + 1
    cnt = 1
    while tmp < d:
        tmp += a
        cnt += 1
    ans += cnt

print(ans)


