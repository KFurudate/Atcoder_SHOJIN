import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
CD = [list(map(int, input().split())) for _ in range(m)]
#print(AB)
#print(CD)

for i in range(n):
    dist_list = []
    for j in range(m):
        dist = abs(AB[i][0] - CD[j][0]) + abs(AB[i][1] - CD[j][1])
        dist_list.append(dist)
    #print(dist_list)
    print(dist_list.index(min(dist_list))+1)