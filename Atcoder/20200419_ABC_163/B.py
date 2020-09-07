n, m = map(int, input().split())
A = list(map(int, input().split()))
ans = n-sum(A)
if ans <= 0:
    print(-1)
else:
    print(ans)