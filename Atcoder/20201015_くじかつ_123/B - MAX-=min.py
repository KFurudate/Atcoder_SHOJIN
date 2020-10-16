from math import gcd
n = int(input())
A = list(map(int, input().split()))

cnt = 0
for a in A:
    cnt = gcd(cnt, a)
print(cnt)