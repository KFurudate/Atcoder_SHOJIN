import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

k = int(input())
L = [(a, b, c) for a in range(1, k+1) for b in range(1, k+1) for c in range(1, k+1)]
ans = 0
for l in L: ans += gcd_list(l)
print(ans)

######################
#TLE
import math
k = int(input())
ans = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            ans += math.gcd(a, math.gcd(b, c))
print(ans)

####################
#1338 ms
import math
k = int(input())
ans = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        tmp = math.gcd(a, b)
        for c in range(1, k+1):
            ans += math.gcd(tmp, c)
print(ans)