S = input()[::-1]

cnt = 0
flg = True

for s in S:
    if s == "0":
        flg = False
    elif s == "+" and flg:
        cnt += 1
        flg = True
    elif s == "+" and flg is False:
        flg = True

    # print(s, flg)

if flg:
    cnt += 1
print(cnt)
