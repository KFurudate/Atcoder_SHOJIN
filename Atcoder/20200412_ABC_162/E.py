import sys
input=lambda :sys.stdin.readline().rstrip()

mod = 10**9+7

n, k = map(int, input().split())

#d[i]:gcdがiの倍数になる個数
d = [0] * (k+1)
for i in range(1, k+1):
    d[i] = pow(k//i, n, mod)

#d[i]から重複（iの倍数）を除くと、gcd(A)＝iになる個数がd[i]となる
for i in range(k, 0, -1):
    for j in range(2*i, k+1, i):
        d[i] -= d[j]
        d[i] %= mod
ans=0
for i in range(1, k+1):
    ans += d[i]*i
    ans %= mod

print(ans)