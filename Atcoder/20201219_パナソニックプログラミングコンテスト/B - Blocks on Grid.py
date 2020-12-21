import numpy as np
h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

A = np.array(A)
print(np.sum(A-np.min(A)))