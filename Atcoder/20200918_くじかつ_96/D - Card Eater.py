n = int(input())
A = list(map(int, input().split()))

k = len(set(A))
if k % 2:
    print(k)
else:
    print(k-1)
