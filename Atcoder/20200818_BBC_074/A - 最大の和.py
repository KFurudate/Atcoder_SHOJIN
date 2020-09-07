n, k = map(int, input().split())
S = [int(input()) for _ in range(n)]

ans = 0
for i in range(n-k+1):
    ans = max(ans, sum(S[i:i+k]))
print(ans)

###################

from itertools import accumulate

n, k = map(int, input().split())
S = [int(input()) for _ in range(n)]
C = [0] + list(accumulate(S))

ans = 0
for i in range(n-k+1):
    ans = max(ans, C[i+k]-C[i])
print(ans)
