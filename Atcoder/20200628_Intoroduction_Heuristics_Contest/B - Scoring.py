D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]
T = [int(input())-1 for _ in range(D)]

last = [0] * 26
score = 0
for d in range(D):
    v = T[d]
    score += S[d][v]
    for i in range(26):
        if i == v:
            last[i] = 0
        else:
            last[i] += 1
        score -= C[i] * last[i]
    print(score)