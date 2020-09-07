h, w, m = map(int, input().split())
HW = [list(map(int, input().split())) for _ in range(m)]

H = [0] * m
W = [0] * m
idx = 0
for h, w in HW:
    H[idx], W[idx] = h, w
    idx += 1
#print(H, w)

set_H = set(H)
set_W = set(W)
ans = max(len(set_H), len(set_W))
print(ans)
