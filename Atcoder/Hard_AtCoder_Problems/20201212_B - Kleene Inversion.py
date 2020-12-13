n, k = map(int, input().split())
A = list(map(int, input().split()))

MOD = 10 ** 9 + 7

cnt = 0
ans = 0
for i in range(n-1):
    for j in range(i, n):
        if A[i] > A[j]:
            cnt += 1
ans += cnt * k % MOD

cnt = 0
for i in range(n):
    for j in range(n):
        if A[i] > A[j]:
            cnt += 1
ans += cnt * k*(k-1)//2 % MOD
print(ans % MOD)