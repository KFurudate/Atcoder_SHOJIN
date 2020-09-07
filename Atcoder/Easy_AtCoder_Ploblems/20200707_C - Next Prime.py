x = int(input())


def is_prim(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

for i in range(x, 10**5+1):
    if is_prim(i):
        print(i)