n = int(input())
SP = []
for i in range(n):
    tmp = list(map(str, input().split()))
    tmp.append(i+1)
    SP.append(tmp)
SP = sorted(SP)

city = SP[0][0]
City = [(int(SP[0][1]), SP[0][2])]
for sp in SP[1:]:
    if sp[0] != city:
        City = sorted(City, reverse=True)
        for c in City:
            print(c[1])
        City = []
    City.append((int(sp[1]), sp[2]))
    city = sp[0]

City = sorted(City, reverse=True)
for c in City:
    print(c[1])
