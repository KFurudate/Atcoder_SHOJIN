#https://atcoder.jp/contests/abc035/tasks/abc035_c

import sys
from itertools import accumulate

input=lambda :sys.stdin.readline().rstrip()
n, q = map(int, input().split())

O = [0]*(n+1)

Q = []
Q_append = Q.append
for _ in range(q):
    l, r = map(int, input().split())
    Q_append((l-1, r-1))

#imos methods
#step 1: Add & Sub
for q in Q:
    O[q[0]] += 1
    O[q[1]+1] -= 1

#step 2: Cumulative sum
S = [0] + list(accumulate(O))
ans = [str(1) if s%2 else str(0) for s in S][1:n+1]
print("".join(ans))