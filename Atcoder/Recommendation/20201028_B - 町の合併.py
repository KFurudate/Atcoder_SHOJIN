n = int(input())
SP = [list(map(str, input().split())) for _ in range(n)]

cnt = 0
MAX = 0
ans = ""
for s, p in SP:
    p = int(p)
    cnt += p
    MAX = max(MAX, p)
    if MAX == p:
        ans = s
if MAX > cnt/2:
    print(ans)
else:
    print("atcoder")