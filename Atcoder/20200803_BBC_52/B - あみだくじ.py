N, L = map(int, input().split())
dist = [i+1 for i in range(N)]
for _ in range(L):
    S = input()
    S.replace("|", "")
    for i in range(N-1):
        if S[i] == "-":
            dist[i], dist[i+1] = dist[i+1], dist[i]
goal = input()
idx = goal.index("o")//2
ans = dist[idx]
print(ans)
