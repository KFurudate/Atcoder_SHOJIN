def main():
    import sys
    input = sys.stdin.readline

    def Warshall_Floyd(d):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d

    n, m, l = map(int, input().split())
    f_inf = float('inf')
    dist = [[f_inf] * n for _ in range(n)]
    # for _ in range(m): dist[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        dist[a - 1][b - 1] = c
        dist[b - 1][a - 1] = c

    Warshall_Floyd(dist)

    dist2 = [[f_inf] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= l:
                dist2[i][j] = 1

    Warshall_Floyd(dist2)

    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        if dist2[s - 1][t - 1] == f_inf:
            print(-1)
        else:
            ans = dist2[s - 1][t - 1]
            print(ans - 1)


if __name__ == "__main__":
    main()
