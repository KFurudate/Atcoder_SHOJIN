import collections

n, k = map(int, input().split())
a = list(map(int, input().split()))
A = collections.Counter(a)

keys, conts = zip(*A.most_common()[::-1])
ans = 0
x = len(set(a))

for cont in conts:
    if x > k:
        ans += cont
    x -= 1

print(ans)