#https://atcoder.jp/contests/abc103/tasks/abc103_d

import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

B = []
B_append = B.append
for _ in range(m):
    a, b = map(int, input().split())
    B_append((b, a))

B.sort()
ans = 1
tmp = B[0][0]
for upper, lower in B[1:]:
  if lower >= tmp:
      tmp = upper
      ans += 1

print(ans)
