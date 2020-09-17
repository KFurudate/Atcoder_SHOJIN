n, a, b = map(int, input().split())

if n < a+b:
    print(min(a,b),  a+b-n)

else:
    print(min(a,b),  0)