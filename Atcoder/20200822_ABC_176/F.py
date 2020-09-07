from collections import Counter
N = int(input())
A = list(map(int, input().split()))

cnt = 1
if Counter(A[:5]).most_common()[0][1] == 3:
    cnt += 1
for i in range(5, 3*N-3, 3):
    if len(set(A[i:i+3]))==1:
        cnt += 1
print(cnt)

##########################

from collections import Counter
N = int(input())
A = list(map(int, input().split()))

tmp = A[:5]
tmp.append(A[-1])
_, counts = zip(*Counter(tmp).most_common())

cnt = 0
cnt += counts.count(3)
for i in range(5, 3*N-3, 3):
    if len(set(A[i:i+3]))==1:
        cnt += 1
print(cnt)
