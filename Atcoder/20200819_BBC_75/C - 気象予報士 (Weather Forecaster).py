h, w = map(int, input().split())
T = [list(input()) for _ in range(h)]

for tt in T:
    ans = []
    flg = False
    idx = 1
    for t in tt:
        #print(t)
        if t == "c":
            ans.append("0")
            flg = True
            idx = 1
        elif flg:
            ans.append(str(idx))
            idx += 1
        else:
            ans.append("-1")
    print(*ans)
