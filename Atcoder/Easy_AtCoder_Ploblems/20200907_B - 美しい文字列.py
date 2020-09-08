from collections import Counter
W = input()
C = Counter(W)
print(C)

for v in C.values():
    if v % 2:
        print("No")
        exit()
print("Yes")