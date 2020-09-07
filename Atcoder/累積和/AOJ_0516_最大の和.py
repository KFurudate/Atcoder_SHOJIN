#https://upura.hatenablog.com/entry/2019/04/01/212701

while True:
  n, k = map(int, input().split())
  if n == 0 and k == 0:
    break
  A = [int(input()) for _ in range(n)]
  ans = [sum(A[i:i+k]) for i in range(n-2)]
  print(max(ans))
##################
#00:31s, 15368KB, 242bytes
while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    A = [int(input()) for _ in range(n)]

    S = [0] * (n + 1)
    for i in range(n):
        S[i + 1] = S[i] + A[i]
    d = [S[i] - S[i - k] for i in range(k, n + 1)]
    print(max(d))

###################
#00:27s, 15520KB, 247bytes
from itertools import accumulate

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    A = [int(input()) for _ in range(n)]

    S = [0] + list(accumulate(A))
    d = [S[i] - S[i - k] for i in range(k, n + 1)]
    print(max(d))


