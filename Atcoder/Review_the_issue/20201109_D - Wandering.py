# TLR
n = int(input())
A = list(map(int, input().split()))

ans = 0
tmp = 0
for i in range(1, n + 1):
    for a in A[:i]:
        tmp += a
        ans = max(tmp, ans)
print(ans)

##########################

from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))
C = list(accumulate(A))
MAX = list(accumulate(C, func=max))

now = 0
ans = 0
for ac, mx in zip(C, MAX):
  ans = max(ans, now+mx)
  now += ac
print(ans)