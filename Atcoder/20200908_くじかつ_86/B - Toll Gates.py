n, m, x = map(int, input().split())
A = list(map(int, input().split()))

cnt1, cnt2 = 0, 0
for a in A:
    if a < x:
        cnt1 += 1
    if a > x:
        cnt2 += 1

ans = min(cnt1, cnt2)
print(ans)