from itertools import accumulate
import sys

input = lambda: sys.stdin.readline().rstrip()

k, n = map(int, input().split())
A = list(map(int, input().split()))
res = 0
tmp = A[0]
for a in A[1:]:
    res += (a - tmp)
    tmp = a
print(res)
A.append(k - res)
A.append(A[1])
S = [0] + list(accumulate(A))
d = [S[i] - S[] for i in range(n, n + 1)]
print(min(d))
###################
import sys
input = lambda: sys.stdin.readline().rstrip()

k, n = map(int, input().split())
A = list(map(int, input().split()))
A.append(A[0]+k)

l = 0
for i in range(n):
    l = max(l, A[i+1]-A[i])
ans = k - l
print(ans)