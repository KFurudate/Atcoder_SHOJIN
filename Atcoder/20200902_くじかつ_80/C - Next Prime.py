def eratosthenes_sieve(n):
    is_prime = [True]*(n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
        if is_prime[p]:
            for q in range(2*p, n + 1, p):
                is_prime[q] = False
    return is_prime

x = int(input())

MAX_N=(10**5)+1
Primes = eratosthenes_sieve(MAX_N)
while True:
    if Primes[x]:
        print(x)
        exit()
    x += 1

