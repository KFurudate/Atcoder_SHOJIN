from collections import deque

s = input()
q = int(input())
Q = [list(map(str, input().split())) for _ in range(q)]

S = deque([s])
S_reverse = S.reverse
S_appendleft = S.appendleft
S_append = S.append

for i in Q:
    if int(i[0]) == 2:
        if int(i[1]) == 1:
            S_appendleft(i[2])
        else:
            S_append(i[2])

    else:
        S_reverse()

print(''.join(S))from collections import deque
s = input()
q = int(input())
Q = [list(map(str, input().split())) for _ in range(q)]

S = deque([s])
S_reverse = S.reverse
S_appendleft = S.appendleft
S_append = S.append

for i in Q:
  if int(i[0]) == 2:
    if int(i[1]) == 1:
      S_appendleft(i[2])
    else:
      S_append(i[2])

  else:
    S_reverse()

print(''.join(S))