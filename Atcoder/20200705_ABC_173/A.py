n = int(input())

for i in range(1000, 11000, 1000):
    if i >= n:
        print(i-n)
        exit()
