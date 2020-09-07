from heapq import *

n, q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
MAX_N = 2*10**5 + 1
Table = [[[], []] for _ in range(MAX_N)]

for a, b in AB:
  heappush(Table[b][0], - a)

A_que = []
for i in range(MAX_N):
  if len(Table[i][0]) != 0:
    heappush(A_que, -Table[i][0][0])

B_que = []
for _ in range(q):
  c, d = map(int, input().split())
  c -= 1
  a, b = AB[c]
  AB[c][1] = d
  heappush(Table[b][1], -a)

  if Table[b][0][0] == -a:
    while Table[b][1] and Table[b][1][0] == Table[b][0][0]:
      heappop(Table[b][1])
      heappop(Table[b][0])
    heappush(B_que, a)
    if Table[b][0]: heappush(A_que, -Table[b][0][0])

  cnt = 0
  if Table[d][0]: cnt = Table[d][0][0]
  heappush(Table[d][0], -a)

  if Table[d][0][0] != cnt:
    heappush(A_que, a)
    if cnt != 0: heappush(B_que, -cnt)

  while B_que and A_que[0] == B_que[0]:
    heappop(A_que)
    heappop(B_que)
  print(A_que[0])