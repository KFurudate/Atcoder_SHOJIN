#https://atcoder.jp/contests/code-thanks-festival-2017-open/tasks/code_thanks_festival_2017_c

from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

Dic = {}
Hq = []
for _ in range(n):
    a, b = map(int, input().split())
    Dic[a] = b
    heappush(Hq, a)

cnt = 0
for _ in range(k):
    min_hq = heappop(Hq)
    cnt += min_hq
    b = Dic[min_hq]
    c = min_hq+ b
    heappush(Hq, c)
    Dic[c] = b
print(cnt)
#################3
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

Hq = []
for _ in range(n):
    a, b = map(int, input().split())
    heappush(Hq,(a, b))

cnt = 0
for _ in range(k):
    a, b = heappop(Hq)
    cnt += a
    heappush(Hq, (a+b, b))
print(cnt)






    
