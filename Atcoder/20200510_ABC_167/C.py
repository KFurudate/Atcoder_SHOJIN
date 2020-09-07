#部分集合
#bit演算
#2進数

"""
n, m, x = map(int, input().split())

C = []
A = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    C.append(tmp[0])
    A.append(tmp[1:])
"""

n, m, x = 3, 3, 10
C,A = [60, 70, 50], [[2, 2, 4], [8, 7, 9], [2, 3, 9]]

f_inf = float("inf")
ans = f_inf
for s in range(1<<n):
    cost = 0
    D = [0] * m
    for i in range(n):
        if s>>i & 1:
            cost += C[i]
            for j in range(m):
                D[j] += A[i][j]

    ok = True
    for d in D:
        if d < x: ok = False
    if ok: ans = min(ans, cost)
if ans == f_inf: print(-1)
else: print(ans)


