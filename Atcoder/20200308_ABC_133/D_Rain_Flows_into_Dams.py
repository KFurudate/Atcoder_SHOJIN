n = int(input())
A = list(map(int, input().split()))

x2 = 0
for i in range(n):
    if i % 2:
        print(i % 2)
        x2 -= A[i]
    else:
        x2 += A[i]
ans = [0]*n
ans[0] = int(x2/2)
for i in range(n-1):
    ans[i+1] = int(A[i]) - int(ans[i])
for i in range(n):
    ans[i] *= 2

L = [str(a) for a in ans]
print(" ".join(L))

