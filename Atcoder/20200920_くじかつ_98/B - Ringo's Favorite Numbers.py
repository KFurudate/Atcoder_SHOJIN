d, n = map(int, input().split())

cnt = 0
for i in range(1, 10**7+1):
    if i%(100**d) == 0:
        cnt += 1
    if n == 100:
        if cnt == n+1:
            print(i)
            exit()
    else:
        if cnt == n:
            print(i)
            exit()

