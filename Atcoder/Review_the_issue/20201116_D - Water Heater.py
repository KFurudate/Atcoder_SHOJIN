# TLE
import numpy as np

n, w = map(int, input().split())
STP = [list(map(int, input().split())) for _ in range(n)]

ans = np.array([0] * (2*(10**5)))
t_mx = 0
for s, t, p in STP:
    ans[s:t] += np.array([p]*(t-s))
    t_mx = max(t, t_mx)
    if max(ans[:t_mx+1]) > w:
        print("No")
        exit()

print("Yes")

####################
from itertools import accumulate

n, w = map(int, input().split())
STP = [list(map(int, input().split())) for _ in range(n)]

ans = [0] * (2*(10**5)+1)
t_mx = 0

for s, t, p in STP:
    ans[s] += p
    ans[t] -= p
    t_mx = max(t, t_mx)

ans = list(accumulate(ans[:t_mx+1]))

if max(ans) <= w:
  print("Yes")
else:
  print("No")




