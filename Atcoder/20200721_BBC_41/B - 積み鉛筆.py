n = int(input())
K = list(map(int, input().split()))

MAX_k = str(max(K))

ans = [MAX_k for _ in range(n+1)]
print(" ".join(ans))