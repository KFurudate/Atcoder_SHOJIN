n, a, b = map(int, input().split())

if a == 0 or b == 0:
    print(0, 0)

elif n > a+b:
    max_ab = min(a, b)
    print(max_ab, 0)

else:
    max_ab = min(a, b)
    print(max_ab, a+b-n)


