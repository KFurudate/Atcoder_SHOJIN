S = input()
Y, M, D = int(S[:4]), int(S[5:7]), int(S[8:])

def day_checker(y, m, d):
    for d in range(d, 32):
        if (d == 31) and (M not in [1, 3, 5, 7, 8, 10, 12]):
            continue
        if M == 2:
            if d >= 30:
                continue
            if (d == 29) and (Y % 4 != 0):
                continue
            if (d == 29) and (Y % 4 == 0):
                if (Y % 10 == 0) and (Y % 400 != 0):
                    continue

        ans = y / m / d
        if ans.is_integer():
            m, d = str(m), str(d)
            if len(m) == 1:
                m = "0" + m
            if len(d) == 1:
                d = "0" + d
            print(f"{y}/{m}/{d}")
            exit()

day_checker(Y, M, D)

for m in range(M+1, 13):
    day_checker(Y, m, 1)

for y in range(Y+1, 4000):
    for m in range(1, 13):
        day_checker(y, m, 1)
