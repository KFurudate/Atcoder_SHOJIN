#WA
n = int(input())
m = int(input())
AB = [list(map(int, input().split())) for _ in range(m)]

F = []
FF = []
for a, b in AB:
    if a == 1:
        F.append(b)
    if b == 1:
        F.append(a)
    if a in F:
        FF.append(b)
    if b in F:
        FF.append(a)
print(len(set(F+FF)))

#####################