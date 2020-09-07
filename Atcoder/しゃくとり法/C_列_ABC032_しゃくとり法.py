#https://atcoder.jp/contests/abc032/tasks/abc032_c
import sys

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
S = [int(input()) for _ in range(n)]

if 0 in S:
    print(n)
    exit()

ans = 0
right = 0
p = 1

for left in range(n):
    while right < n and (p * S[right]) <= k:
        p *= S[right]
        right += 1
    ans = max(ans, right - left)
    if left == right:
        right += 1
    else:
        p //= S[left]

print(ans)