#https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
X_L = []
X_L_append = X_L.append
for _ in range(n):
    x, l = map(int, input().split())
    X_L_append((x+l, x-l))
X_L.sort()

ans = n
tmp = X_L[0][0]
for upper, lower in X_L[1:]:
  if lower < tmp:
    ans -= 1
  else:
    tmp = upper

print(ans)







