from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))
C = [0] + list(accumulate(A))

ans = 0
for i in range(2, n+1):
    tmp = C[1]+C[i]
    ans = max(ans, tmp)
print(ans)

