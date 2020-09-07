from collections import *

n = int(input())
S = [input() for _ in range(n)]
C = Counter(S)
print(C.most_common()[0][0])