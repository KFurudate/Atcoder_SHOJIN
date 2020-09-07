n = int(input())
A = list(map(int, input().split()))

ave = sum(A)/len(A)
ans = []
for i in range(n):
    tmp = abs(A[i] - ave)
    ans.append(tmp)


print(ans.index(min(ans)))