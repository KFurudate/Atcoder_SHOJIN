x = int(input())

if x >= 2000:
    print(1)
    exit()

for i in range(1, 20):
    if (100 * i <= x) and (x <= 105 * i):
        print(1)
        exit()
print(0)

