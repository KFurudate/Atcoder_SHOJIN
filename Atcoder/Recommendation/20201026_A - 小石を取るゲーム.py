n, a, b = map(int, input().split())

for i in range(n):
    if i%2:
        n -= 1
    else:
        n -= 2
    if n < 0:
        break

if i%2:
    print("Ant")
else:
    print("Bug")
