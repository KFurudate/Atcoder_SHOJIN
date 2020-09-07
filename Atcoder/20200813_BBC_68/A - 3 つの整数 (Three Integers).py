A, B, C = map(int, input().split())

cnt = 0
for abc in [A, B, C]:
    if abc == 1:
        cnt += 1
    else:
        cnt -= 1

if cnt > 0:
    print(1)
else:
    print(2)


