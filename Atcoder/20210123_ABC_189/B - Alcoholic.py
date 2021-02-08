from decimal import Decimal

n, x = map(int, input().split())
VP = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i, (v, p) in enumerate(VP):
    cnt += Decimal(str(v)) * Decimal(str(p)) / Decimal(str(100))

    if cnt > x:
        print(i + 1)
        exit()

print(-1)