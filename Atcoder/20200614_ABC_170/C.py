x, n = map(int, input().split())

if n == 0:
    P = []
else:
    P = list(map(int, input().split()))

for i in range(1, 100):
    if x - i not in P:
        dif_mis = x-i
        break

for i in range(0, 100):
    if x + i not in P:
        dif_pls = x+i
        break

if (x-dif_mis)**2 > (x-dif_pls)**2:
    print(dif_pls)
else:
    print(dif_mis)
