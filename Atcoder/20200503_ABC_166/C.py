n, m = map(int, input().split())
H = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((H[b], b))
    graph[b].append((H[a], a))

cnt = 0
for i in range(n):
  graph[i].sort(reverse=True)
  if graph[i]:
    if graph[i][0][0] < H[i]:
      cnt += 1
  else:
    cnt += 1
print(cnt)
