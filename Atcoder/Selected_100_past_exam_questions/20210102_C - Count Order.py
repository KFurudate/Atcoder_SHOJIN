from itertools import permutations

n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

patterns = tuple(permutations(tuple(range(1, n + 1))))

a, b = 0, 0
for idx, p in enumerate(patterns):
    if p == P:
        a = idx+1
    if p == Q:
        b = idx+1

print(abs(a - b))
