from collections import Counter
import sys

input = sys.stdin.readline

def Washall_Floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def flatten_2dim(array):
    return [item for sublist in array for item in sublist]


n, x, y = map(int, input().split())
f_inf = float('inf')
dist = [[f_inf] * n for _ in range(n)]
for i in range(n): dist[i][i] = 0

for i in range(n - 1):
    dist[i][i + 1] = 1
    dist[i + 1][i] = 1

dist[x - 1][y - 1] = 1
dist[y - 1][x - 1] = 1
Washall_Floyd(dist)

counter = Counter(flatten_2dim(dist))
counter = sorted(counter.most_common())[1:]

for key, val in counter:
    print(val // 2)
for i in range(n - len(counter) - 1):
    print(0)
##################
def main():
    from collections import Counter
    from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
    import sys
    input = sys.stdin.readline
    def flatten_2dim(array): return [item for sublist in array for item in sublist]

    n, x, y = map(int, input().split())
    f_inf = float('inf')
    dist = [[f_inf] * n for _ in range(n)]

    for i in range(n-1):dist[i][i+1], dist[i+1][i] = 1, 1
    dist[x-1][y-1], dist[y-1][x-1] = 1, 1

    G = csgraph_from_dense(dist, null_value=10**9)
    dist = floyd_warshall(G)

    counter = Counter(flatten_2dim(dist))
    counter = sorted(counter.most_common())[1:]

    for key, val in counter: print(val//2)
    for _ in range(n - len(counter)-1): print(0)
if __name__ == "__main__": main()

###############################
from collections import deque
import sys
input = sys.stdin.readline

f_inf = float('inf')

def push(v, d):
    if dist[v] != f_inf: return
    dist[v] = d
    que.append(v)

n, x, y = map(int, input().split())
x -= 1
y -= 1

ans = [0]*n
for sv in range(n):
    dist = [f_inf] * n
    que = deque([])
    push(sv, 0)

    while que:
        v = que.popleft()
        d = dist[v]+1
        if v-1 >= 0: push(v-1, d)
        if v+1 < n: push(v+1, d)
        if v == x: push(y, d)
        if v == y: push(x, d)

    for i in range(n):
        ans[dist[i]] += 1
for i in range(n):
    ans[i] = ans[i]//2

for i in range(1, n):
    ans[i]




