n, x, t = map(int, input().split())

for i in range(1, 10**5):
    if i*x >= n:
        print(i*t)
        exit()
