#https://atcoder.jp/contests/arc074/tasks/arc074_b
from heapq import heapify, heappush, heappop
from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = deepcopy(A)

heapify(B)
C = []
for a in A:
    heappush(C, -a)

Min_lst = []
Max_lst = []
Min_lst_append = Min_lst.append
Max_lst_append = Max_lst.append
for i in range(n):
    if i%2:
        Max_lst_append(heappop(C))
    else:
        Min_lst_append(heappop(B))

A_remove = A.remove
for i in Min_lst:
    A_remove(i)
for i in Max_lst:
    A_remove(i)

ans = sum(A[:n+1]+A[n+1:])
print(ans)





#################

import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
A.sort()

if n % 2:

else:
A[n//2:]

