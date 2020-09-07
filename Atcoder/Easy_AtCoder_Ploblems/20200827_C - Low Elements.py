N = int(input())
P = list(map(int, input().split()))

pj = P[0]
cnt = 1
for pi in P[1:]:
    if pi < pj:
        cnt += 1
        pj = pi
print(cnt)

