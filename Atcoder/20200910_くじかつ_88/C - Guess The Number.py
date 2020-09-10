#WA
n, m = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(m)]


NUM = [0] * n
Check = [0] * n
for s, c in SC:
    if (n != 1) and (s == n-1) and (c == 0):
        print(-1)
        exit()

    if (NUM[n-s] == 0) and (Check[n-s] != 0) and (c != 0):
        print(-1)
        exit()

    if NUM[n-s] == 0:
        NUM[n-s] = c

    elif (NUM[n-s] != 0) and (NUM[n-s] != c):
        print(-1)
        exit()

    Check[n-s] += 1

if (n != 1) and (NUM[n-1] == 0):
    print(-1)
    exit()

for s in NUM[::-1]:
    print(s, end="")

###########################
#全探索
n, m = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(m)]

for x in range(1000):
    keta = 1
    nx = x//10
    d = [x%10]

    while nx:
        keta += 1
        d.append(nx%10)
        nx //= 10

    if keta != n: continue

    flg = True
    d.reverse()
    for s, c in SC:
        if d[s-1] != c:
            flg = False
    if flg:
        print(x)
        exit()

print(-1)


