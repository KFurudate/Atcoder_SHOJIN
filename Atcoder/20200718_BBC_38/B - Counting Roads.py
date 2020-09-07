n, m = map(int, input().split())

Road = []
for _ in range(m):
    a, b = map(int, input().split())
    Road.append((a, b))

tmp = sorted(Road)
#print(tmp)

ans = [0]*n
for t in tmp:
  ans[t[0]-1] += 1
  ans[t[1]-1] += 1

for a in ans:
  print(a)