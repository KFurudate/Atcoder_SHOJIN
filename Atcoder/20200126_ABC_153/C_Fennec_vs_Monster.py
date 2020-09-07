n , k = map(int, input().split())
h = sorted(list(map(int, input().split())), reverse=True)

if k >= len(h):
    H = []
else:
    H = h[k:]

if len(H) == 0:
  print(0)
else:
  print(sum(H))