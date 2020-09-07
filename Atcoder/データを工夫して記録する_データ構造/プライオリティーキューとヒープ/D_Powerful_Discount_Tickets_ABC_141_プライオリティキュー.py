#https://atcoder.jp/contests/abc141/tasks/abc141_d
from heapq import heappush, heappop
import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
Hq = []
for a in A:
    heappush(Hq, -a)

for _ in range(m):
    max = -heappop(Hq)
    heappush(Hq, -math.floor(max / 2))
print(-sum(Hq)) 