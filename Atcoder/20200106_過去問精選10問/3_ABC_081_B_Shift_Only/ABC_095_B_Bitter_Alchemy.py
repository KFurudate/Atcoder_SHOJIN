n, x = map(int, input().split())
M = []
for _ in range(n):
    M.append(int(input()))

print(len(M)+((x-sum(M))//min(M)))