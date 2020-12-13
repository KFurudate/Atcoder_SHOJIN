from math import ceil

n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))

cnt = float("inf")
pre_a = 1
ws = []
for a in A:
    w = a - pre_a
    pre_a = a + 1
    if w == 0: continue
    cnt = min(cnt, w)
    ws.append(w)

if m != 0:
    if n != a:
        ws.append(n - a)
    ans = 0
    for w_ in ws:
        if w_ == 0: continue
        ans += ceil(w_ / cnt)
else:
    ans = 1
print(ans)