#https://atcoder.jp/contests/abc014/tasks/abc014_3

import sys
from itertools import accumulate
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
Q = [list(map(int, input().split()) )for _ in range(n)]

A = [0]*(n+1)
#imos methods
#step 1: Add & Sub
for q in Q:
    A[q[0]] += 1
    A[q[1]+1] -= 1

#step 2: Cumulative sum
S = [0] + list(accumulate(A))

print(S)