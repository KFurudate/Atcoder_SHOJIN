#n, a, b = map(int, input().split())
n = 20
a = 2
b = 5

ans = 0

for i in range(1, n+1):
    sum = 0
    x = i
    while x > 0:
        sum += x % 10
        x = x//10
    if sum >= a and sum <= b:
        ans += i

print(ans)