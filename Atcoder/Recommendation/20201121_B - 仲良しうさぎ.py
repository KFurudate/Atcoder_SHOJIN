n = int(input())
A = list(map(int, input().split()))

ans = [0]*n

cnt = 0
for idx, a in enumerate(A):
  if idx+1 == A[A[idx]-1]:
    cnt += 1
print(cnt//2)