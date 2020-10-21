h, w = map(int, input().split())
S = [list(str(input())) for _ in range(h)]

ans = 0
for i in range(h):
    cnt = 0
    for j in range(w):
        if S[i][j] == ".":
            cnt += 1
        else:
            cnt = 0

        if cnt >= 2:
            ans += 1

for j in range(w):
    cnt = 0
    for i in range(h):
        if S[i][j] == ".":
            cnt += 1
        else:
            cnt = 0

        if cnt >= 2:
            ans += 1
print(ans)
