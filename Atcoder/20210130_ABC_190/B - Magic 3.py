n, s, d = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for x, y in XY:
    if x >= s:
        continue
    if y <= d:
        continue
    ans += y

if ans > 0:
    print("Yes")
else:
    print("No")