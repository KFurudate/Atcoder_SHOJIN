s = int(input())

ans = [s]
idx = 1
tmp = s
while True:
    if tmp % 2 == 0:
        tmp = tmp//2
    else:
        tmp = (3*tmp) + 1
    idx += 1

    if tmp in ans:
        print(idx)
        exit()
    else:
        ans.append(tmp)



