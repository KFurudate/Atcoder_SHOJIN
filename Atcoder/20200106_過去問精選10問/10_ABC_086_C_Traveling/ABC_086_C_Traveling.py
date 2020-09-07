n = int(input())
txy = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    dt = txy[i][0]
    dst = txy[i][1] + txy[i][2]
    if dt < dst:
        print('No')
        exit()

    if txy[i][0] % 2 == 0:
        if (txy[i][1]+txy[i][2]) % 2 != 0:
            print('No')
            exit()

    elif txy[i][0] % 2 != 0:
        if (txy[i][1]+txy[i][2]) % 2 == 0:
            print('No')
            exit()

print('Yes')




