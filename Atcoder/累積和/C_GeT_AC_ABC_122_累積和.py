#https://atcoder.jp/contests/abc122/tasks/abc122_c
from itertools import accumulate
n, q = map(int, input().split())
s = input()
A =[1 if s[i]+s[i+1] == 'AC' else 0 for i in range(n-1)]
S = [0] + list(accumulate(A))

Q = []
Q_append = Q.append
for _ in range(q):
    l, r = map(int, input().split())
    Q_append((l-1, r-1))

for qi in Q:
    print(S[qi[1]]-S[qi[0]])