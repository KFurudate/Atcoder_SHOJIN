n = input()

if int(n) % 3 == 0:
    print(0)
    exit()

for i in range(len(n) - 1):
    for j in range(len(n)):
        k = i + j + 1
        if k > len(n): continue
        if int(n[:j] + n[k:]) % 3 == 0:
            print(i + 1)
            exit()
print(-1)