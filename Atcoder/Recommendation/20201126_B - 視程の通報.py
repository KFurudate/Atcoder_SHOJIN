m = int(input())

m /= 1000

if m < 0.1:
    print("00")
    exit()

elif (0.1 <= m) and (m < 6):
    m *= 10
    m = str(int(m))
    if len(m) == 1:
        m = "0" + m

elif (6 <= m) and (m <= 30):
    m += 50
    m = int(m)

elif (35 <= m) and (m <= 70):
    m -= 30
    m /= 5
    m += 80
    m = int(m)

elif 70 < m:
    print(89)
    exit()

print(m)
