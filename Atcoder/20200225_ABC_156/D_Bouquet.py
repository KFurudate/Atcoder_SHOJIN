#https://qiita.com/derodero24/items/91b6468e66923a87f39f
from operator import mul
from functools import reduce

n, a, b = map(int, input().split())
mod = 10 ** 9 + 7


def cmb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


cnt = 0
for i in range(1, n + 1):
    if i == a or i == b:
        continue
    else:
        cnt += cmb(n, i)

print(cnt % mod)from operator import mul
from functools import reduce
n, a, b = map(int, input().split())
mod = 10**9+7

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under
cnt = 0
for i in range(1, n+1):
    if i == a or i == b:
      continue
    else:
      cnt += cmb(n, i)


print(cnt%mod)