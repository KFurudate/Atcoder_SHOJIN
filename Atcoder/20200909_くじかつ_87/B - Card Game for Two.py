n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
print(A)

Alice = 0
Bob = 0
for i in range(n):
    if i % 2:
        Bob += A[i]
    else:
        Alice += A[i]
print(Alice-Bob)
