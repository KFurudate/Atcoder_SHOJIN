#TLE
n = int(input())
A = list(map(int, input().split()))

def prime_fact(num):
    from collections import Counter

    prime = []
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            prime.append(i)
            num //= i
    if num != 1:
        prime.append(num)

    return Counter(prime)

ans = 0
for a in A:
    v_max = 0
    keys = []
    for k, v in prime_fact(a).items():
        keys.append(k)
        if not k % 2:
            v_max = max(v_max, v)
        if 3 in keys: break
    ans += v_max
print(ans)

#########################
n = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    while a%2==0:
        ans += 1
        a //= 2
print(ans)


