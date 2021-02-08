n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
CD = [list(map(int, input().split())) for _ in range(k)]

cnt = [0] * n
for a, b in AB:
    a -= 1
    b -= 1
    cnt[a] += 1
    cnt[b] += 1

ans = [0] * n
for c, d in CD:
    c -= 1
    d -= 1
    ans[c] += 1
    ans[d] += 1

for c, d in CD:
    c -= 1
    d -= 1
    if ans[c] == 1:
        cnt[c] = 0
        ans[c] = 0

    elif ans[d] == 1:
        cnt[d] = 0
        ans[d] = 0

    elif cnt[c] >= cnt[d]:
        cnt[c] = 0
        
    else:
        cnt[d] = 0

print(m - sum(cnt))