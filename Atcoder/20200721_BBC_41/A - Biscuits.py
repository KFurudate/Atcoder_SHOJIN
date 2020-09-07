from itertools import combinations
n, p = map(int, input().split())
A = list(map(int, input().split()))

C =[list(combinations(A, i)) for i in range(n)]

print(C)


#if p == 0:

