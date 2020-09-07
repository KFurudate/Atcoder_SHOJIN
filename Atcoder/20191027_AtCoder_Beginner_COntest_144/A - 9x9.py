A=2
B=5

A, B = map(int, input().split())
if A < 10 and B < 10:
    print(A*B)
else:
    print(-1)