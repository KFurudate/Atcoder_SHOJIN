N, K = map(int, input().split())
ab_lst = [-1] * N
for _ in range(K):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ab_lst[a] = b

dp = [[[0] * 3 for _ in range(3)] for _ in range(N+1)]
dp[0][0][0] = 1

for n in range(N):
    for i in range(3):
        for j in range(3):
            if ab_lst[n] != -1:
                S = [ab_lst[n]]
            else:
                S = [0, 1, 2]

            for s in S:
                if n >= 2 and s == i == j: continue
                dp[n+1][i][s] += dp[n][j][i]

print(sum(sum(n) for n in dp[N]) % 10000)
