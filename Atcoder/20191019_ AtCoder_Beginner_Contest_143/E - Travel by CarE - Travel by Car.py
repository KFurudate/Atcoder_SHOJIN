#https://juppy.hatenablog.com/entry/2018/11/01/%E8%9F%BB%E6%9C%AC_python_%E5%85%A8%E7%82%B9%E5%AF%BE%E6%9C%80%E7%9F%AD%E7%B5%8C%E8%B7%AF%E6%B3%95%EF%BC%88%E3%83%AF%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E6%B3%95

def warshall_floyd(dist):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],
                              dist[i][k] + dist[k][j])
    return dist

n, m, l = map(int, input().split()) #N:頂点数　M:辺の数 L:容量
dist = [[float("inf") for i in range(n)] for j in range(n)]

for i in range(n):
    dist[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c

warshall_floyd(dist)
dist2 = [[float("inf") for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if dist[i][j] <= l:
            dist2[i][j] = 1

warshall_floyd(dist2)
q = int(input())
for i in range(q):
    s, t = map(int, input().split())
    ans = dist2[s-1][t-1]-1
    if dist2[s-1][t-1] == float("inf"):
        ans = -1
    print(ans)