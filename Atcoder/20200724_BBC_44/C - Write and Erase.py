from collections import Counter

n = int(input())
A = [0]*n
for i in range(n):
    A[i] = int(input())
#print(A)
C = Counter(A)
values, counts = zip(*C.most_common())
print(len([i for i in counts if i % 2 == 1]))