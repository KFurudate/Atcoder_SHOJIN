n = int(input())
VWXYZ = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for vwxyz in VWXYZ:
    if sum(vwxyz) < 20:
        cnt += 1
print(cnt)