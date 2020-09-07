import copy

n, m = map(int, input().split())
ans = [0] * n
bns = copy.deepcopy(ans)

for _ in range(m):
    s, c = map(int, input().split())
    if bns[s - 1] == 0:
        bns[s - 1] = c
    elif s != 1 and bns[s - 1] != 0 and bns[s - 1] > c:
        bns[s - 1] = c

if n == 1:
    L = [str(b) for b in bns]
    print("".join(L))
    exit()

if n >= 2 and bns[0] != 0:
    L = [str(b) for b in bns]
    print("".join(L))
    exit()

print(-1)