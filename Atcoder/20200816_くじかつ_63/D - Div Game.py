from collections import Counter

n = int(input())

def prime_fact(n):
    #エラトステネスの篩
    P = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            P.append(i)
            n //= i
    if n != i:
        P.append(n)
    return P


cnt = Counter(prime_fact(n))

print(cnt)

ans = 0
for c in cnt.values():
    tmp = 1
    while c >= tmp:
        c -= tmp
        ans += 1
        tmp += 1

print(ans)