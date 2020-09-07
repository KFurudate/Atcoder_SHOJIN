N, K = map(int, input().split())

A = 1/(2*N)

tmp = 2**N
B = (tmp-1)/tmp

print(A*B)
######################
N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    p = 1
    while i < K:
        p *= 0.5
        i *= 2
    ans += p / N

print(ans)