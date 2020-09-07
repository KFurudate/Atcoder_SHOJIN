import itertools
from functools import reduce
from operator import xor

#N, K = list(map(int, input().split()))

#T = []
#for i in range(N):
#   T.append(list(map(int, input().split())))

N, K =3, 4
T = [[1, 3, 5, 17], [2, 4, 2, 3], [1, 3, 2, 9]]

ans = 'Nothing'

for pr in list(itertools.product(*T)):
    if not reduce(xor, pr):
        ans = 'Found'

print(ans)