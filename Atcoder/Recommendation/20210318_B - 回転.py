n = int(input())
C = [input() for _ in range(n)]

all = []
j = 0
for _ in range(n):
    ans = []
    for i in range(n-1, -1, -1):
        ans.append(C[i][j])
    j += 1

    all.append(ans)

for al in all:
    print("".join(map(str, al)))
