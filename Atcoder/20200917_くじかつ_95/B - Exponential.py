import math
from decimal import *

X = int(input())

a = math.floor(X**0.5)
b = math.ceil(X**0.5)

if b**2 <= X:
    print(b**2)
else:
    print(a**2)
#######################
X = int(input())

ans = 0
for i in range(1, int(X**0.5)+1):
    for j in range(2, 1000):
        tmp = pow(i, j)
        if tmp > X:
            break
        ans = max(ans, tmp)

print(ans)
