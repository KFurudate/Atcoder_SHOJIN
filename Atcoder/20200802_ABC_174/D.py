n = int(input())
C = input()
print(C)

n = int(input())
C = input()
print(C.count("WRW"))
print(C.count("WRR"))

from collections import Counter

n = int(input())
C = list(input())
Cnt = Counter(C)
print(min(Cnt["R"], Cnt["W"]))