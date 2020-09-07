# RE
#　N = 200000 の場合、評点が最大で 10^1800000 と非常に大きくなる
#累積積
import numpy as np

n, k = map(int, input().split())
A = np.array(list(map(int, input().split())))
S = A.cumprod().tolist()
#print(S)

tmp = S[k-1]
for i in range(n-k):
    if tmp < S[k+i]//S[i]:
        print("Yes")
    else:
        print("No")
    #print(tmp, S[k+i]//S[i])

    tmp = S[k+i]//S[i]
############################
n, k = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n-k):
    if A[i] < A[k+i]:
        print("Yes")
    else:
        print("No")
