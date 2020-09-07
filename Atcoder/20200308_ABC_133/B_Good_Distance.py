import itertools

n, d = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for v in itertools.combinations(X, 2):
    y = 0
    for i in range(d):
        y += (v[0][i] - v[1][i]) ** 2
    if(y ** 0.5).is_integer():
        cnt += 1

print(cnt)