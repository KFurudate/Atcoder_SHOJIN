n, a, b  = map(int, input().split())

for _ in range(n):
    if a < b:
        a += 1
        if a == b:
            print('Borys')
            exit()

    if b <= n:
        b += 1
    else:
        b -= 1
        if b == a:
            print('Alice')
            exit()
else:
    print('Draw')
