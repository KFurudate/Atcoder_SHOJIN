n = int(input())
A = list(map(int, input().split()))

ans = float("inf")
for a in A:
    cnt = 0
    while a%2==0:
        a //= 2
        cnt += 1
    ans = min(ans, cnt)
print(ans)