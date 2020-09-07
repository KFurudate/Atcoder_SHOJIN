k = int(input())

A = [i for i in range(1, 10)]

while k:
    if k <= len(A):
        print(A[k - 1])
        exit()

    k -= len(A)

    old = []
    old, A = A, old
    for x in old:
        for i in range(-1, 2):
            d = (x % 10) + i
            if d < 0 or d > 9: continue

            nx = (x * 10) + d
            A.append(nx)
