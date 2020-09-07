h, w = map(int, input().split())
C =[input() for _ in range(h)]

print(C)
for c in C:
    for _ in range(2):
        print(c)