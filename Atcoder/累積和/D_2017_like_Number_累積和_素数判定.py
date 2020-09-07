#https://atcoder.jp/contests/abc084/tasks/abc084_d

#TLE
import math

def is_prime(n):
  if n == 1: return False
  for k in range(2, int(math.sqrt(n))+1):
    if n % k == 0:
      return False
  return True

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    A = [i for i in range(l, r+1, 2)]
    B = [(a+1)//2 for a in A]
    cnt = 0
    for i in range(len(A)):
      if is_prime(A[i]) and is_prime(B[i]):
        cnt += 1
    print(cnt)
#######################
#TLE
import math
from itertools import accumulate

def is_prime(n):
  if n == 1: return False
  for k in range(2, int(math.sqrt(n))+1):
    if n % k == 0: return False
  return True

MAX = (10**5)+1
q = int(input())
A = [1 for i in range(MAX) if is_prime(i)and is_prime((i + 1)//2)]
S = [0] + list(accumulate(A))

Q =[]
Q_append = Q.append
for _ in range(q):
    l, r = map(int, input().split())
    Q_append((l, r))

for qi in Q:
    print(S[qi][1]-S[qi][0])

#######################
#688ms	21120KB
import math
from itertools import accumulate

def is_prime(n):
    if n < 2: return False
    for k in range(2, int(math.sqrt(n))+1):
        if n % k == 0: return False
    return True

MAX = (10**5)+1
q = int(input())
A = [1 if is_prime(i) and is_prime((i+1)//2) else 0 for i in range(MAX)]
S = [0] + list(accumulate(A))

Q = []
Q_append = Q.append
for _ in range(q):
    l, r = map(int, input().split())
    Q_append((l, r))

for qi in Q:
    print(S[qi[1]+1]-S[qi[0]])