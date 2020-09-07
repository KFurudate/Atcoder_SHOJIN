#ダブリング
#Python TLE
#PyPy3
n, k = 6, 727202214173249351
A = [6, 5, 2, 5, 3, 2]

#n, k = map(int, input().split())
#A = list(map(int, input().split()))

D = 60 #10**18は60桁なので2の59乗まで見る
MAX_N = 200005 #頂点番号
to = [[0 for _ in range(MAX_N)] for _ in range(D)]

#to[i][j]:jから2^i個先の頂点
for i in range(n):
    to[0][i] = A[i]
    to[0][i] -= 1

#ダブリングの表
for i in range(D-1):
    for j in range(n):
        to[i+1][j] = to[i][to[i][j]]

v = 0
for i in range(D-1, -1, -1):
    l = 1<<i #2^i個先を見る
    if l <= k:
        v = to[i][v]
        k -= l

print(v+1)


