#https://atcoder.jp/contests/abc084/tasks/abc084_d
#https://oku.edu.mie-u.ac.jp/~okumura/python/sieve.html
#453ms	22036KB

from itertools import accumulate

def primes(n):
  prime = ([False]*2) + ([True]*(n-2))
  for i in range(2, n):
    if prime[i]:
      for j in range(i*2, n, i):
        prime[j] = False
  return prime

MAX = (10**5)+1
is_prime = primes(MAX)
q = int(input())
A = [1 if is_prime[i] and is_prime[(i + 1)//2] else 0 for i in range(MAX)]
S = [0] + list(accumulate(A))

Q = []
Q_append = Q.append
for _ in range(q):
    l, r = map(int, input().split())
    Q_append((l, r))

for qi in Q:
    print(S[qi[1]+1]-S[qi[0]])