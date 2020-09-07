import sys
import collections

input = sys.stdin.readline
n = int(input())
A = collections.Counter([int(input()) for _ in range(n)])

keys, cnts = zip(*A.most_common())
ans = 0
for cnt in cnts:
    if cnt % 2 != 0:
        ans += 1

print(ans)



