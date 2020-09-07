n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

#print(A)
ans = 0
for i in range(1, 2*n+1, 2):
  ans += A[i]
print(ans)