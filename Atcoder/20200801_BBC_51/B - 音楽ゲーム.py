n = int(input())
Musical_score = [input() for _ in range(n)]

M = [[] for _ in range(9)]
for m in Musical_score:
    for i in range(9):
        M[i].append(m[i])

cnt = 0
flg = True
for m in M:
    flg = True

    for i in m:
        if i == "x":
            cnt += 1
            flg = True

        if i == "o" and flg:
            cnt += 1
            flg = False

        if i == ".":
            flg = True

print(cnt)

