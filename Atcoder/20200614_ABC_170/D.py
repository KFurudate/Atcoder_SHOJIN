n = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in A:
    for j in A:
        if i == j: continue
        if i % j == 0:
            cnt += 1
print(cnt)

################
def divisor(n):
    d = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i ** 2 == n:
                continue
            d.append(n // i)
    return d

n = int(input())
A = list(map(int, input().split()))
set_A = set(A)

cnt = 0
for a in tuple(set_A):
    tmp = set(divisor(a)) & set_A
    if len(tmp) == 1: cnt += 1

print(cnt)

###########################
def divisor(n):
    d = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i ** 2 == n:
                continue
            d.append(n // i)
    return d

n = int(input())
A = list(map(int, input().split()))
set_A = set(A)

cnt = [0]*(max(A)+1)
for a in A:
    tmp = set(divisor(a)) & set_A
    if len(tmp) == 1 and cnt[a] == 0:
      cnt[a] = 1
print(sum(cnt))
######################
n = int(input())
A = list(map(int, input().split()))

MAX_A = max(A)+1
cnt = [0] * MAX_A

for a in A:
  for i in range(a, MAX_A, a):
    if cnt[i] <= 2: cnt[i] += 1

ans = 0
for a in A:
  if cnt[a] == 1: ans += 1
print(ans)