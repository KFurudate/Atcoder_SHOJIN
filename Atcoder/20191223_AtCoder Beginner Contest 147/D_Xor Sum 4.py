n = int(input())
a = list(map(int, input().split()))
mod = 1000000007

ans = 0
for i in range(60):
    cont = 0
    for j in range(n):
        if (a[j] >> i & 1):
            cont += 1
    now = cont * (n-cont) % mod
    for j in range(i):
        now  = now * 2 % mod
    ans += now
    ans %= mod
print(ans)