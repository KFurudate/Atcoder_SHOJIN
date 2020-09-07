#https://abc021.contest.atcoder.jp/tasks/abc021_d
#TLE
from scipy.misc import comb
n = int(input())
k = int(input())
print(comb(n+k-1, k, exact=True)%(10**9+7))

#########
mod = 10**9+7

def comb(n, r):
    if 2*r > n: return comb(n, n-r)
    return fac[n] * inv[r] * inv[n-r] % mod

n = int(input())
k = int(input())

max_n = 10**6
fac = [1]*(max_n+2)
inv = [1]*(max_n+2)
for i in range(2, max_n+1):
    fac[i] = fac[i-1] * i % mod
inv[max_n] = pow(fac[max_n], mod-2, mod)
for i in range(max_n-1, 1, -1):
    inv[i] = inv[i+1] * (i+1) % mod

print(comb(n+k-1, k) % mod)



