#TLE
S = input()
n = int(input())
Q =[list(map(str, input().split())) for _ in range(n)]

for q in Q:
    if q[0] == "1":
        S = S[::-1]
    else:
        if q[1] == "1":
            S = q[2] + S
        else:
            S = S + q[2]
print(S)


################################

# TLE

S = input()
n = int(input())
Q =[list(map(str, input().split())) for _ in range(n)]

flg = True
for q in Q:
    if q[0] == "1":
        flg = not flg
    else:
        if q[1] == "1" and flg:
            S = q[2] + S
        elif q[1] == "1" and not flg:
            S = S + q[2]
        elif q[1] == "2" and flg:
            S = S + q[2]
        else:
            S = q[2] + S

if not flg:
    S = S[::-1]
print(S)


################################

# TLE
S = input()
n = int(input())
Q =[list(map(str, input().split())) for _ in range(n)]

flg = True
for q in Q:
    if q[0] == "1":
        flg = not flg
    else:

        if (q[1] == "1" and flg) or (q[1] == "2" and not flg):
            S = q[2] + S
        else:
            S = S + q[2]
if not flg:
    S = S[::-1]
print(S)
################################
# TLE
S = input()
n = int(input())
Q = [list(map(str, input().split())) for _ in range(n)]

flg = True
for q in Q:
    if q[0] == "1":
        flg = not flg
    else:
        F = int(q[1])
        if not flg:
            F = 3 - F
        if F == 1:
            S = q[2] + S
        if F == 2:
            S = S + q[2]

if not flg:
    S = S[::-1]
print(S)

################################

from collections import deque
S = deque(input())
n = int(input())
Q = [list(map(str, input().split())) for _ in range(n)]

flg = True
for q in Q:
    if q[0] == "1":
        flg = not flg
    else:
        F = int(q[1])
        if not flg:
            F = 3 - F
        if F == 1:
            S.appendleft(q[2])
        if F == 2:
            S.append(q[2])

if not flg:
    S.reverse()
print("".join(S))

