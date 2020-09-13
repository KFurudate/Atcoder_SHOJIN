d = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(d)]
T = [int(input()) for _ in range(d)]

last = [0] * 26
score = 0

for i, (s, t) in enumerate(zip(S, T), 1):
    score += s[t - 1]
    last[t - 1] = i
    for j in range(26):
        score -= C[j] * (i - last[j])
    print(score)
