n = int(input())

x = n
fx = 0

while n > 0:
    fx += n % 10
    n = n // 10

if x % fx == 0:
    print('Yes')
else:
    print('No')