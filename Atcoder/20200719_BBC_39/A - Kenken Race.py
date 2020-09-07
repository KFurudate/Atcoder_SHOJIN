n, a, b, c, d = map(int, input().split())
S = input()

T = ""
for i in range(n):
    if i == a - 1:
        T += "A"
    elif i == b - 1:
        T += "B"
    else:
        T += S[i]
# print(T)

cnt = 0
rok = 0
if c < d:
    for i in range(a, d):
        if T[i] == "#":
            rok += 1

        else:
            rok = 0

        if rok >= 2:
            print("No")
            exit()
    print("Yes")

else:
    for i in range(a, d):
        if T[i] == "#":
            cnt = 0
            rok += 1

        elif T[i] == ".":
            cnt += 1
            rok = 0

        if cnt >= 3:
            print("Yes")
            exit()

        if rok >= 2:
            print("No")
            exit()
    print("No")


####################
n, a, b, c, d = map(int, input().split())
S = input()

if c < d and S[a:d].count("##") == 0:
    print("Yes")
    exit()

if c > d and S[b:d].count("...") >= 1 and S[a:c].count("##") == 0:
    print("Yes")
    exit()

print("No")

