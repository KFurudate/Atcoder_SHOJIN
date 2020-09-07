#n, m, q = map(int, input().split())
#A = [0]*q
#B = [0]*q
#C = [0]*q
#D = [0]*q
#for i in range(q):
#   A[i], B[i], C[i], D[i] = map(int, input().split())

n, m, q = 3, 4, 3
A, B, C, D = [1, 1, 2], [3, 2, 3], [3, 2, 2], [100, 10, 10]

a = [1]
ans = 0
def dfs(a):
    global ans
    if len(a) == n+1:
        now = 0
        for i in range(q):
            if a[B[i]] - a[A[i]] == C[i]:
                now += D[i]
        ans = max(ans, now)
        return

    a.append(a[-1])
    while a[-1] <= m:
        a[-1] += 1
        dfs(a)
    a.pop(-1)

dfs(a)
print(ans)