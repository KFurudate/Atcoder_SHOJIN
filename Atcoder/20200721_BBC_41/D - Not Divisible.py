n = int(input())
A = list(map(int, input().split()))

MAX_N = max(A)+ 1
cnt = [0] * MAX_N
for a in A:
    for i in range(a, MAX_N, a):
        if cnt[i] <= 2:
            cnt[i] += 1

ans = 0
for a in A:
    if cnt[a] == 1:
        ans += 1
print(ans)

