#https://atcoder.jp/contests/agc023/tasks/agc023_a

from itertools import accumulate
import collections

n = int(input())
A = list(map(int, input().split()))
S = list(accumulate(A))

C = collections.Counter(S)
cnt = C[0]
mc = C.most_common()
for c in mc:
    if c[1] > 1:
        cnt += c[1]*(c[1]-1)//2
print(cnt)
