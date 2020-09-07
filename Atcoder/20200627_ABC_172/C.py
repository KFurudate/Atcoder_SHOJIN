import sys

input = lambda: sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

cnt = 0
if A[0] < B[0] and A[0] <= k:
    cnt += 1
    k -= A[0]

idx_a = 1
idx_b = 0

while k > 0:
    if B[idx_b] > A[idx_a]:
        k -= A[idx_a]
        if k >= 0: cnt += 1
        if idx_a < n - 1: idx_a += 1

    if B[idx_b] < A[idx_a]:
        k -= B[idx_b]
        if k >= 0: cnt += 1
        if idx_b < m - 1: idx_b += 1

    if B[idx_b] == A[idx_a]:
        k -= A[idx_a]
        if k >= 0: cnt += 1
        if idx_a < n - 1: idx_a += 1

        k -= B[idx_b]
        if k >= 0: cnt += 1
        if idx_b < m - 1: idx_b += 1

print(cnt)

########################
from itertools import accumulate

n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = [0] + A
A = list(accumulate(A))

B = [0] + B
B = list(accumulate(B))

ans = 0
b_cnt = m
for a_cnt in range(n+1):
    if A[a_cnt] > k: continue

    while A[a_cnt]+B[b_cnt] > k:
        b_cnt -= 1
    ans = max(ans, a_cnt+b_cnt)

print(ans)




