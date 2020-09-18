#WA
import math
n = int(input())
TA = [list(map(int, input().split())) for _ in range(n)]

A, B = 1, 1
for t, a in TA:
    n = max(math.ceil(A/t), math.ceil(B/a))
    A = n*t
    B = n*a

print(A+B)


#######################

n = int(input())
TA = [list(map(int, input().split())) for _ in range(n)]

A, B = 1, 1
for t, a in TA:
    n = max((A-1)//t+1, (B-1)//a+1)
    A = n*t
    B = n*a

print(A+B)