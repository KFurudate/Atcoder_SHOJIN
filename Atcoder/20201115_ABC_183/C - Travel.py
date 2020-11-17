from itertools import permutations

n, k = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(n)]

if n == 2:
    ans = 2*(T[0][1])
    if ans == k:
      print(1)
    else:
      print(0)
    exit()

city = [i for i in range(1, n)]
p = list(permutations(city))

ans = 0
for v in p:
    cnt = 0
    for i in range(len(v) - 1):
        j = i + 1
        cnt += T[v[i]][v[j]]
        if i == 0:
            cnt += T[0][v[i]]
    cnt += T[v[j]][0]
    if cnt == k:
        ans += 1
print(ans)