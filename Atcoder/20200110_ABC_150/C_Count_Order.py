import itertools

n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))

perm = list(itertools.permutations(range(1, n+1)))
print(abs(perm.index(p)-perm.index(q)))