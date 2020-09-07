from collections import Counter

n, k, q = map(int, input().split())
A = [int(input()) for _ in range(q)]
C = Counter(A)

ans = [k]*n
for i in range(n):
  ans[i] += C[i+1]
for a in ans:
  if a > q:
    print("Yes")
  else:
    print("No")