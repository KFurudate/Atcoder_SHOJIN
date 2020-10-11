# TLE
n = int(input())
P = list(map(int, input().split()))

ans = []
ans_append = ans.append
idx = max(P)
print(idx, ans)
for p in P:
    if p != 0 and 0 not in ans:
        print(0)
        ans_append(p)
    elif p > idx and idx not in ans:
        print(idx)
        ans_append(p)

    else:
        ans_append(p)
        print(max(ans) + 1)

    idx = min(max(ans) + 1, idx)


##############################
n = int(input())
P = list(map(int, input().split()))

idx = 0
ans = []
ans_append = ans.append
for p in P:
    if p != idx:
        print(idx)
        ans_append(p)
    else:
        ans_append(p)
        idx = max(ans) + 1

        print(idx)
print(idx, ans, "*")

