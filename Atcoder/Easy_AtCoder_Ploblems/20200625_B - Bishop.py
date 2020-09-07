import math

h, w = map(int, input().split())

print(math.ceil(h*w/2))

######################
h, w = map(int, input().split())
ans = h * w
if ans % 2 == 0:
    print(ans//2)
else:
    ans += 1
    print(ans//2)

######################

h, w = map(int, input().split())
ans = h * w

if h % 2 == 0 or w % 2 == 0:
    print(ans // 2)
else:
    ans += 1
    print(ans // 2)

###################

import math

h, w = map(int, input().split())
if h == 1 or w == 1:
    print(1)
else:
    print(math.ceil(h*w/2))


