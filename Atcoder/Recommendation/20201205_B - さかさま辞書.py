n = int(input())
S = sorted([input()[::-1] for _ in range(n)])
for s in S:
  print(s[::-1])