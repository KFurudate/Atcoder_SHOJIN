# WA
n = int(input())
A = list(map(int, input().split()))

l, r = 0, -1
x, y = A[l], A[r]

if n == 2:
    print(abs(x - y))
    exit()

ans = float("inf")
for _ in range(1, n - 1):
    if x > y:
        r -= 1
        y += A[r]
    elif x <= y:
        l += 1
        x += A[l]
    if l + 1 + abs(r) == n:
        ans = min(ans, abs(x - y))

print(ans)

################################
from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))

if n == 2:
    print(abs(A[0]-A[1]))
    exit()

B = list(accumulate(A))

ans = float("inf")
y = 0
for i in range(n-1, 0, -1):
    x = B[i-1]
    y += A[i]
    ans = min(ans, abs(x-y))
print(ans)