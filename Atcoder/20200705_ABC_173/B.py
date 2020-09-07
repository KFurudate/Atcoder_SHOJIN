import collections

n = int(input())
S = [input() for _ in range(n)]

ans = ("AC", "WA", "TLE", "RE")
cnt = collections.Counter(S)

for a in ans:
    print(f"{a} x {cnt[a]}")