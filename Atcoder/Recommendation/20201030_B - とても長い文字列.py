A = input()
B = int(input())

n = B//len(A)

print(A[B - len(A)*n - 1])