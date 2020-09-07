#https://atcoder.jp/contests/agc025/tasks/agc025_b

#TLE
mod = 998244353

def comb(n, r):
    if 2 * r > n: return comb(n, n - r)
    return fac[n] * inv[r] * inv[n - r] % mod


n, a, b, k = map(int, input().split())

fac = [1] * (n + 2)
inv = [1] * (n + 2)
for i in range(2, n + 1):
    fac[i] = fac[i - 1] * i % mod
inv[n] = pow(fac[n], mod - 2, mod)
for i in range(n - 1, 1, -1):
    inv[i] = inv[i + 1] * (i + 1) % mod

ans = 0
for i in range(n + 1):
    for j in range(n + 1):
        if a * i + b * j > k: break
        if a * i + b * j == k:
            ans += comb(n, i) * comb(n, j)
print(ans % mod)
###################
#Python3: 657ms
#pypy3: 274ms

mod = 998244353

def comb(n, r):
    if 2 * r > n: return comb(n, n-r)
    return fac[n] * inv[r] * inv[n-r] % mod

n, a, b, k = map(int, input().split())

fac = [1] * (n+2)
inv = [1] * (n+2)
for i in range(2, n+1):
    fac[i] = fac[i-1] * i % mod
inv[n] = pow(fac[n], mod - 2, mod)
for i in range(n-1, 1, -1):
    inv[i] = inv[i + 1] * (i + 1) % mod

ans = 0
for i in range(n+1):
    Num = (k-a*i)
    if (0 <= Num//b) and (Num//b <= n) and (Num%b == 0):
      j = Num//b
      ans += comb(n, i) * comb(n, j)
print(ans%mod)
###########################
#TLE
from scipy.misc import comb

mod = 998244353

n, a, b, k = map(int, input().split())

ans = 0
for i in range(n+1):
    Num = (k-a*i)
    if (0 <= Num//b) and (Num//b <= n) and (Num%b == 0):
      j = Num//b
      ans += comb(n, i, exact=True) * comb(n, j, exact=True)
print(ans%mod)
