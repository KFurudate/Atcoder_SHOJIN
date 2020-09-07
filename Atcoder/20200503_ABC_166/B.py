n, k = map(int, input().split())
D = [0]*k
A = []
for i in range(k):
    D[i] = int(input())
    A.append(list(map(int, input().split())))

cnt = 0
ans = []
for a in A:
  for i in a:
    if i not in ans:
      ans.append(i)
print(n-len(ans))

