n = int(input())
A = list(map(int, input().split()))

MOD = 10 ** 9 + 7


def nCr(n, r):
    if 2 * r > n: nCr(n, n - r)
    return fac[n] * inv[r] * inv[n - r] % MOD


fac = [1] * (n + 1)
inv = [1] * (n + 1)

for i in range(n):
    fac[i + 1] = fac[i] * (i + 1) % MOD
    inv[i + 1] = pow(fac[i + 1], MOD - 2, MOD)

ans = 0
for i in range(n):
    print(nCr(n - 1, i)*A[i], "*")
    tmp = nCr(n - 1, i) * A[i] * pow(A[i] - 1, n - 1 - i, MOD)
    ans += tmp
    ans %= MOD
print(ans)