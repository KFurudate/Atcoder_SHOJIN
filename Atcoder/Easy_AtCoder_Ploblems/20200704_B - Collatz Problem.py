s = int(input())

a = []
ans = 0

while True:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3*n) + 1
    ans += 1
    if n in a: break
    a.append(n)

print(ans)
