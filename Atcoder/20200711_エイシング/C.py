#n = int(input())
n = 10000

ANS = []
for i in range(1, n + 1):
    cnt = 0
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):

                if i == ((x + y + z) ** 2 - z * (x + y) - (x * y)):
                    cnt += 1

    ANS.append(cnt)
print(ANS)

#########################
n = int(input())

ANS = [] * (n+1)
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            tmp = ((x + y + z) ** 2 - z * (x + y) - (x * y))
            if tmp > n: continue
            ANS[tmp] += 1


for ans in ANS:
    print(ANS)