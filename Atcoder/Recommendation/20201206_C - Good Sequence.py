from collections import Counter

n = int(input())
A = Counter(list(map(int, input().split())))

ans = 0
for k, v in A.items():
    if k == v:
        continue
    elif k > v:
        ans += v
    else:
        ans += v-k
print(ans)