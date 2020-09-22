#解説AC

n = int(input())
A = list(map(int, input().split()))

b1, b4 = 0, 0
for a in A:
    if a % 2:
        b1 += 1
    if a % 4 == 0:
        b4 += 1

b2 = min(1, n-(b1+b4))

if b1+b2-1 <= b4:
    print("Yes")
else:
    print("No")