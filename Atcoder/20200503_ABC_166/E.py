import sys
input=lambda :sys.stdin.readline().rstrip()
from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
ans = 0
for j in range(n):
    Dif = jA[j]
    ans += d[Dif]
    Sum = A[j] + j
    d[Sum] += 1
print(ans)
