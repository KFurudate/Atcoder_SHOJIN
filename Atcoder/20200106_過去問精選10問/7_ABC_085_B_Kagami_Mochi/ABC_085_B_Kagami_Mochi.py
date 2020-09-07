n = int(input())
d = sorted([int(input()) for _ in range(n)], reverse=True)

cont = 1
mochi = [0]

for i in d:
    if mochi[-1] > i:
        cont += 1
    mochi.append(i)

print(cont)