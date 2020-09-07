n=3
m=2
l=5
def warshall_floyd(dist):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],
                              dist[i][k] + dist[k][j])
    return dist

#n, m, l = map(int, input().split()) #N:頂点数　M:辺の数 L:容量
dist = [[float("inf") for i in range(n)] for i in range(n)]
dist2 = [[float("inf") for i in range(n)] for j in range(n)]

for i in range(n):
    dist[i][i] = 0

print(dist)

a = 1
b = 2
c = 3

dist[a][b] = c
dist[b][a] = c
print(dist)

a = 2
b = 0
c = 3

dist[a][b] = c
dist[b][a] = c
print(dist)

for i in range(n):
    for j in range(n):
        if dist[i][j] <= l:
            dist2[i][j] = 1

print(dist2)

warshall_floyd(dist2)
print(dist2)