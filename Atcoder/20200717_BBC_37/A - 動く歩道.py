l, x, y, s, d = map(int, input().split())

if d == s:
    print(0)
    exit()

if x >= y:
    if d > s:
        print((d-s) / (x+y))
        exit()
    if s > d:
        print((l-(s-d)) / (x+y))
        exit()

if x < y:
    if d > s:
        print(min((d-s)/(x+y), (l-(d-s)) / (y-x)))
        exit()

    if s > d:
        print(min((s-d) / (y-x), (l-(s-d)) / (x+y)))
        exit()


