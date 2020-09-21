# TLE
import sys
input=lambda :sys.stdin.readline().rstrip()
n, m = map(int, input().split())

key = [0]*n
for _ in range(m):
    l, r = map(int, input().split())
    for i in range(l-1, r):
        key[i] = key[i]+1
print(len([i for i in key if i == m]))

##############################

n, m = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(m)]
f_inf = float("inf")

max_l = 0
min_r = f_inf
for l, r in LR:
    max_l = max(max_l, l)
    min_r = min(min_r, r)

if min_r >= max_l:
    print(min_r - max_l + 1)
else:
    print(0)
