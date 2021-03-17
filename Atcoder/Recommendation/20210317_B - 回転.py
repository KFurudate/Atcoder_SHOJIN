C = [input().split() for _ in range(4)]

all = []
for i in range(3, -1, -1):
    ans = []
    for j in range(3, -1, -1):
        ans.append(C[i][j])
    all.append(ans)

for al in all:
    print(*al)
