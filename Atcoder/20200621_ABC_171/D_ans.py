from collections import *

n = int(input())
A = list(map(int, input().split()))
q = int(input())


A_dic = Counter(A)
A_sum = sum(A)

for _ in range(q):
    b, c = map(int, input().split())
    tmp = A_dic[b]
    A_dic[c] += tmp
    A_dic[b] = 0
    A_sum += tmp * (c - b)
    print(A_sum)
