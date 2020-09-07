S = input()

cnt = 0
ans = 0
for s in S:
    if s not in ("A", "C", "G", "T"):
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)