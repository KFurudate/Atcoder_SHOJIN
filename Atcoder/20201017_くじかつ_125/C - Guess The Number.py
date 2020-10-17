n, m = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(m)]

ans = [-1] * n
for s, c in SC:
    if (ans[s-1] != -1) and (ans[s-1] != c):
        print(-1)
        exit()
    ans[s-1] = c

if n >= 2:
    if ans[0] == 0:
        print(-1)
        exit()
    if ans[0] == -1:
        ans[0] = 1

if -1 in ans:
    ans = [0 if i == -1 else i for i in ans]

print(*ans, sep='')