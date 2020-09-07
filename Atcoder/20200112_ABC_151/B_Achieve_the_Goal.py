N, K, M = map(int, input().split())
A = list(map(int, input().split()))

for k in range(K+1):
    if (sum(A)+k)//N >= M:
        print(k)
        exit()
print(-1)