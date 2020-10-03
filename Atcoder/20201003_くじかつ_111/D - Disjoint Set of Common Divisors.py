import math

a, b = map(int, input().split())

GCD = math.gcd(a, b)
print(GCD)

def factrization_prime(num):
    factor = {}
    div = 2
    s = int(num**0.5)+1
    while div < s:
        div_cnt = 0
        while num % div == 0:
            div_cnt += 1
            num //= div
        if div_cnt != 0:
            factor[div] = div_cnt
        div += 1
    if num > 1:
        factor[num] = 1
    return factor