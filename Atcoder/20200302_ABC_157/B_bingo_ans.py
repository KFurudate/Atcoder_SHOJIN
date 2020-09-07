a = [list(map(int, list(input().split()))) for _ in range(3)]
b = [[0] * 3 for _ in range(3)]
n = int(input())
##################
for ni in range(n):
    x = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == x:
                b[i][j] = 1

ans = False
##################
for i in range(3):
    cnt = 0
    for j in range(3):
        cnt += b[i][j]
        if cnt == 3:
            ans = True
##################
for i in range(3):
    cnt = 0
    for j in range(3):
        cnt += b[j][i]
        if cnt == 3:
            ans = True
##################
cnt = 0
for j in range(3):
    cnt += b[j][j]
    if cnt == 3:
        ans = True
##################
cnt = 0
for j in range(3):
    cnt += b[j][2 - j]
    if cnt == 3:
        ans = True
##################
if ans == True:
    print('Yes')
else:
    print('No')