n, m = map(int, input().split())
A = [list(map(str, input().split())) for _ in range(m)]

ans = 0
pen = 0

A = list(map(list, set(map(tuple, A))))

for i in range(A):
    if A[i][1]=='AC':
        ans += 1
        A.remove(A[i, 'WA'])
    if A[i][1] == 'WA':
        pen += 1

print(ans, pen)