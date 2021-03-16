n = int(input())
A = list(map(int, input().split()))

cnt = [0] * 401
for a in A:
    cnt[a + 200] += 1

ans = 0
for i in range(401):
    for j in range(i, 401):
        ans += cnt[i] * cnt[j] * (j - i) ** 2
print(ans)

