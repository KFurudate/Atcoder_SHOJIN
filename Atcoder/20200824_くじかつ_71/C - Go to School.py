N = int(input())
A = list(map(int, input().split()))

ans = [0]*N
for idx, a in enumerate(A):
    ans[a-1] = idx+1
print(*ans)