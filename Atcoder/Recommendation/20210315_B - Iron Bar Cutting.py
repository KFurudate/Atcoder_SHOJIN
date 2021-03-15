from itertools import accumulate
n = int(input())
A = list(map(int, input().split()))
C = list(accumulate(A))

left, right = 0, 0
ans = float("inf")
for i in range(len(A)-1):
    left = C[i]
    right = C[-1] - left
    ans = min(ans, abs(right-left))

print(ans)