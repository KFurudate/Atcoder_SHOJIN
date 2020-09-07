from itertools import accumulate
#累積和

n, k = map(int, input().split())
A = list(map(int, input().split()))
C = [0] + list(accumulate(A))

cnt = 0
for i in range(n-k+1):
  cnt += C[k+i]-C[i]
print(cnt)