n, m, x = map(int, input().split())
A = list(map(int, input().split()))

cnt_down = 0
cnt_up = 0
for i in range(x, 1, -1):
    if i in A: cnt_down += 1

for j in range(x, n, 1):
    if j in A: cnt_up += 1

ans = min(cnt_down, cnt_up)
print(ans)