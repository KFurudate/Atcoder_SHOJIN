import sys

input = lambda: sys.stdin.readline().rstrip()

N, x = map(int, input().split())
A = sorted(list(map(int, input().split())))

if x > sum(A):
    cnt = -1
else:
    cnt = 0

for i in range(N):
    if x - A[i] >= 0:
        cnt += 1
        x -= A[i]
    if x <= 0:
        break
    # print(cnt, x)

print(cnt)