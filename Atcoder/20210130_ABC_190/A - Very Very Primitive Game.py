a, b, c = map(int, input().split())

if c == 0:
    for _ in range(a):
        a -= 1
        if a <= 0:
            print("Aoki")
            exit()
        b -= 1
        if b <= 0:
            print("Takahashi")
            exit()
    print("Aoki")

if c == 1:
    for _ in range(b):
        b -= 1
        if b <= 0:
            print("Takahashi")
            exit()
        a -= 1
        if a <= 0:
            print("Aoki")
            exit()

    print("Takahashi")