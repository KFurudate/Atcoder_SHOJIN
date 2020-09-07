n = int(input())

def Check(x):
    cont= 0
    while x > 0:
        x = x//10
        cont += 1
    return cont

a = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        a.append(i)

a = max(a)
b = n//a

print(max(Check(a), Check(b)))


