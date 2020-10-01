a, b, k = map(int, input().split())

for i in range(a, k+1):
    print(i)
for j in range(b, b-k-1, -1):
    print(j)