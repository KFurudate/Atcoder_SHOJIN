s = int(input())

A = [s]
idx = 1
while True:
    n = A[idx-1]

    if idx % 2:
        f = 3 * n + 1
    else:
        f = n / 2
    idx += 1
    A.append(f)
    print(A, idx)
    if len(A) != len(set(A)):
        break
print(idx)