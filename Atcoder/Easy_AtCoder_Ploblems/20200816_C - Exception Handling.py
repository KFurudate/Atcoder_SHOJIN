n = int(input())
A = [int(input()) for _ in range(n)]

sorted_A = sorted(A, reverse=True)

for i in range(n):
    if A[i] != sorted_A[0]:
        print(sorted_A[0])
    else:
        print(sorted_A[1])

