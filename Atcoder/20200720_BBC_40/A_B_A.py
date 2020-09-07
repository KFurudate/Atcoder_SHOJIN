a, b = map(int, input().split())

ans = [i for i in range(1, b) if b % i == 0]

if a in ans:
    print(a+b)
else:
    print(b-a)