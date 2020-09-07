from itertools import accumulate

n, x = map(int, input().split())
L = list(map(int, input().split()))
C = [0] + list(accumulate(L))
#print(C)

cnt = 0
for c in C:
    if c <= x:
        cnt += 1
print(cnt)