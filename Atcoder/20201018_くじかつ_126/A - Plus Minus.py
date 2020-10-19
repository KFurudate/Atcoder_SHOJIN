a, b = map(int, input().split())

for x in range(101):
    for y in range(101):
        if (a == x+y) and (b == x-y):
            print(a, b)
