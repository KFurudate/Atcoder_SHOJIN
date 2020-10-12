from collections import Counter
n = int(input())
S = [input() for _ in range(n)]
m = int(input())
T = [input() for _ in range(m)]

SC = Counter(S)
TC = Counter(T)

ans = 0
for k, v in SC.items():
    cnt = 0
    cnt += v
    cnt -= TC[k]
    print(cnt, k)
    ans = max(ans, cnt)

print(ans)