n = int(input())
A = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    b, c = map(int, input().split())
    A = [c if a==b else a for a in A]
    print(sum(A))
######################################


n = int(input())
A = input
q = int(input())

ans = 0
for _ in range(q):
    b, c = map(str, input().split())
    A.replace(b, c)
    for a in A:
        ans += int(a)
print(ans)

######################################
import collections

n = int(input())
A = list(map(int, input().split()))
q = int(input())

A_cnt = collections.Counter(A)

for _ in range(q):
    b, c = map(int, input().split())
##########################
n = int(input())
A = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    b, c = map(int, input().split())
    if b in A:
        A = [c if a==b else a for a in A]
    print(sum(A))

########################
#from collections import *

n = int(input())
A = list(map(int, input().split()))
q = int(input())

A_dic = Counter(A)
A_ans = sum(A)

bc = [list(map(int, input().split())) for _ in range(q)]

C_dic = defaultdict(int)
for b,c in bc:
  tmp = A_dic[b]*(c-b)
  C_dic[c] =
  A_ans += tmp
  ptint(A_ans)



print(A_cnt)
print(bc)









