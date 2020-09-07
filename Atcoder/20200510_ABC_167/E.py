n, m, k = map(int, input().split())

MOD = 998244353
ans = 0
N = 1
K = 1
for i in range(k+1):
    ans += N * pow(K, MOD-2, MOD) * pow(m-1, n-1-i, MOD)
    ans %= MOD
    N *= n-1-i
    N %= MOD
    K *= i+1
    K %= MOD
ans *= m
ans %= MOD
print(ans)

