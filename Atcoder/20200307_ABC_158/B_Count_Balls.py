n, a, b = map(int, input().split())
if n >= (a + b):
    x = n // (a + b)
    y = n % (a + b)
    print((a * x) + y)

else:
    print(min(n, a))
##################
n, a, b = map(int, input().split())
x = n // (a + b)
y = n % (a + b)

print(min((a * x) + y, (a * x) + a))