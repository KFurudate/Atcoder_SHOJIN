from collections import deque

s = input()
q = int(input())
Q = [list(map(str, input().split())) for _ in range(q)]

S = deque([s])
flip = False

for qi in Q:
  if int(qi[0]) == 1:
    flip = not flip
  else:
    f = int(qi[1])
    c = qi[2]
    if flip:
      f = 3-f
    if f == 1:
      S.appendleft(c)
    else:
      S.append(c)
if flip:
    S.reverse()
print(''.join(S))