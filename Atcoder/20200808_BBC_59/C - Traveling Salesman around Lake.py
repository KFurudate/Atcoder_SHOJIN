k, n = map(int, input().split())
A = list(map(int, input().split()))
A.append(A[0]+k)

l = 0
for i in range(n):
    l = max(l, A[i+1]-A[i])
ans = k - l
print(ans)