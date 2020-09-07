n = int(input())
H = list(map(int, input().split()))

tmp = H[0]
cnt = 0
ans = 0
for h in H[1:]:
    if tmp >= h:
        cnt += 1
    else:
        cnt = 0
    tmp = h
    ans = max(ans, cnt)
print(ans)