n = int(input())

X_MAX = 50001
for x in range(X_MAX):
    if int(x * 1.08) == n:
        print(x)
        exit()
print(":(")