n = int(input())
AB = sorted([list(map(int, input().split())) for _ in range(n)])

mx, mi = AB[-1], AB[0]
MIN, MAX = mx[1], mi[0] - 1

cnt = 0
pre = AB[0][0]
for a, b in AB[1:]:
    cnt += (a - pre)
    pre = a

cnt += (MIN + MAX + 1)
print(cnt)
