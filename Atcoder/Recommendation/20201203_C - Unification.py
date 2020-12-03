from collections import Counter

S = list(map(int, input()))
C = Counter(S)
ans = min(C[0], C[1])
ans *= 2
print(ans)

