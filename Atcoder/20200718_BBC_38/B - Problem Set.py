n = int(input())
D = list(map(int, input().split()))
m = int(input())
T = list(map(int, input().split()))

for t in T:
    if t not in D:
        print("NO")
        exit()
    else:
        D.remove(t)
print("YES")
###########################
from collections import Counter

n = int(input())
D = list(map(int, input().split()))
m = int(input())
T = list(map(int, input().split()))

Count = Counter(D)

for t in T:
    if not Count[t]:
        print("NO")
        exit()
    else:
        Count[t] -= 1
print("YES")