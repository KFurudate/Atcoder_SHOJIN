from scipy.special import comb

n = int(input())

A = [0] * n

for i in range(n):
    A[i] = int(input())

print(comb(A, 2, exact=True))