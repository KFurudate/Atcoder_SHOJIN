#https://atcoder.jp/contests/abc145/tasks/abc145_d
#TLE
mod = 10**9+7
from scipy.misc import comb

x, y = map(int, input().split())
if (x+y)%3 != 0:
  print(0)
  exit()

#X = a +2*b
#Y = 2*a +b
a = -(x-2*y)//3
b = (2*x-y)//3
print(comb(a+b, a, exact=True)%mod)

####################
mod = 10 ** 9 + 7
def comb(n, r):
    if 2 * r > n: return comb(n, n - r)
    return fac[n] * inv[r] * inv[n - r] % mod


x, y = map(int, input().split())
if (x + y) % 3 != 0:
    print(0)
    exit()

n = (x + y) // 3
x -= n
y -= n
if x < 0 or y < 0:
    print(0)
    exit()

fac = [1] * (n + 2)
inv = [1] * (n + 2)
for i in range(2, n + 1):
    fac[i] = fac[i - 1] * i % mod
inv[n] = pow(fac[n], mod - 2, mod)
for i in range(n - 1, 1, -1):
    inv[i] = inv[i + 1] * (i + 1) % mod

print(comb(x + y, x) % mod)



