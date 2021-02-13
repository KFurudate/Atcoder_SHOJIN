n = int(input())
S = [input() for _ in range(n)]

dp = [1] * 2
for s in S:
    p = [0] * 2
    p, dp = dp, p
    for j in range(2):
        for x in range(2):
            nj = j
            if s == "AND":
                nj &= x
            else:
                nj |= x
            dp[nj] += p[j]

print(dp[1])
