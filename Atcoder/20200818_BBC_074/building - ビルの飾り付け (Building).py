import bisect

n = int(input())
A = [int(input()) for _ in range(n)]

Ans = []
Ans.append(A[0])
for a in A:
    if a > Ans[-1]:
        Ans.append(a)
    else:
        Ans[bisect.bisect_left(Ans, a)] = a
    #print(Ans)

print(len(Ans))