import sys
sys.setrecursionlimit(10**6)

n = int(input())
k = int(input())

def dfs(graph, v):
    seen[v] = True
    for e in graph[v]:
        if seen[e]: continue
        dfs(graph, e)


g = [[] for _ in range(n)]
for i in range(n):
    a = i
    b = i+1
    if i == 0: b = n-1
    if i == n-1: b = 0
    g[a].append(b)
    g[b].append(a)

cnt = 0
for i in range(n):

    seen = [False for _ in range(n-1)]
    seen[0] = True
########################

n = int(input())
k = int(input())

G  =[i for i in range(2, n+1)]

