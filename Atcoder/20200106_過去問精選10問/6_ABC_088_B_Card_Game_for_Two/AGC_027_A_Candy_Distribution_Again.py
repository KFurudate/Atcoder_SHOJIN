N, x = map(int, input().split())
a = list(map(int, input().split()))

cont = 0

for i in sorted(a):
    x -= i
    if x >= 0:
        cont += 1
    else:
        break

if x > 0:
    cont -= 1

print(cont)
###########
""""
N, x = map(int, input().split())
a = list(map(int, input().split()))

cont = 0

for y in sorted(a):
    if x >= y:
        cont += 1
        x -= y

if x > 0:
    cont = cont - 1
print(cont)
"""