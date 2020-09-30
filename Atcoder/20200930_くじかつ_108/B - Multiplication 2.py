# TLE
from itertools import accumulate
import operator

n = int(input())
A = list(map(int, input().split()))
C = list(accumulate(A, func=operator.mul))
ans = C[-1]

if ans <= 10**18:
  print(ans)
else:
  print(-1)

################
n = int(input())
A = list(map(int, input().split()))
if 0 in A:
    print(0)
    exit()
ans = 1
for a in A:
    ans *= a
    if ans > 10**18:
        exit(print(-1))
print(ans)