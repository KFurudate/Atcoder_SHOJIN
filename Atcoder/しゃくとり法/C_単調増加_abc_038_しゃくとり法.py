n = 5
a = [1, 2, 3, 2, 1]

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

cnt = 0
for l in range(n):
    r = l + 1
    cnt += 1
    while r < n and a[r] > a[r-1]:
        cnt += 1
        r += 1
print(cnt)

###############
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

cnt, r = 0, 0
for l in range(n):
    if l > 0 and a[l-1] >= a[l]:
        r = l
    cnt += l-r+1
print(cnt)