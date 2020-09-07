import math

#k = int(input())
k = 4
ans = 0
for a in range(1, k + 1):
    for b in range(1, k + 1):
        if a != b:
            ans += (math.gcd(a, b)) * k
        else:
            ans += math.gcd(a, b)
            ans += math.gcd(a, b - 1) * (k - 1)

print(ans)
#############
import math
from functools import reduce


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


k = int(input())
L = [(a, b) for a in range(1, k + 1) for b in range(1, k + 1)]
ans = 0
for i in range(k + 1):
    tmp = gcd_list(L[i])
    if L[i][0] != L[i][1]:
        ans += tmp * k
    else:
        ans += math.gcd(tmp, i + 1)
        ans += tmp * (k - 1)

print(ans)
