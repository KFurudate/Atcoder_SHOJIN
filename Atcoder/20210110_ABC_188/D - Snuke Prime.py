from collections import defaultdict

n, C = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(n)]

events = defaultdict(int)
for a, b, c in ABC:
    events[a] += c
    events[b+1] -= c

events_sorted = sorted(events.items(), key=lambda x: x)

ans = 0
s = 0
pre = 0
for key, val in events_sorted:
    ans += min(C, s)*(key-pre)
    s += val
    pre = key

print(ans)