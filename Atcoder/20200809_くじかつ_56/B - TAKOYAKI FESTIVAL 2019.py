from itertools import combinations

n = int(input())
D = list(map(int, input().split()))

c = combinations(D, 2)
print(c)