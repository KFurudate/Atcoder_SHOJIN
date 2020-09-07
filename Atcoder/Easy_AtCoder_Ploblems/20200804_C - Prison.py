n, m = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(m)]

print(LR)
L = []
R = []
L_append = L.append
R_append = R.append
for l, r in LR:
    L.append(l)
    R.append(r)

ans = min(L)+1 - min(R)
print(ans)