from collections import Counter

n = int(input())
S = [input() for _ in range(n)]
m = int(input())
T = [input() for _ in range(m)]

cnt_S = Counter(S)
cnt_T = Counter(T)
values, counts = zip(*cnt_S.most_common())

ans = 0
for i in range(len(values)):
    ans = max(ans, counts[i] - cnt_T[values[i]])
print(ans)
