from itertools import accumulate

n = int(input())
A = [list(map(int, input().split())) for _ in range(2)]
C1 = list(accumulate(A[0]))
C2 = [0]+list(accumulate(A[1]))

ans = 0
for i in range(n):
    ans = max(C1[i]+C2[-1]-C2[i] , ans)
print(ans)