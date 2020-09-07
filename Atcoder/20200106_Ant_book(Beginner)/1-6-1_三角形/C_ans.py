n, s = map(int, input().split())

for x in range(n+1):
    for y in range(n+1-x):
        z = n-(x+y)
        if (10000*x) + (5000*y) + (1000*z) == s:
            print(x, y, z)
            exit()

print(-1, -1, -1)