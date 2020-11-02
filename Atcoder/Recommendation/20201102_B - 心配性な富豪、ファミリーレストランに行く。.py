n = int(input())
A = [int(input()) for _ in range(n)]

set_A = list(set(A))
set_A = sorted(set_A, reverse=True)
print(set_A[1])
