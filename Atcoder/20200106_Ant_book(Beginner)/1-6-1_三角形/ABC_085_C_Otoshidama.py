n=1000
s=1234000
#n, s = map(int, input().split())
S = s//1000

x=0
y=0
z=0
for x in range(n+1):
    for y in range(n+1):
        if x + y == n and (9*x) + (4*y) < S-n:
            x = -1
            y = -1
            z = -1
            exit()

        elif x + y == n and (9*x) + (4*y) == S-n:
            exit()

    if x + y < n:
        for z in range(n+1):
            if (5*y) + (9*z) == (10*n)-S:
                exit()
            elif (5*x) + (4*z) == S-(5*n):
                exit()


print('{} {} {}'.format(x, y, z))


