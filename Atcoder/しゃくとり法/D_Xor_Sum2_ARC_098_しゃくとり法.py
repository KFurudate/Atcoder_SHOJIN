#https://atcoder.jp/contests/arc098/tasks/arc098_b
#排他的論理和
n = int(input())
A = list(map(int, input().split()))
l, r, SumA, ans = 0, 0, 0, 0

for l in range(n):
    while r < n and (SumA&A[r]==0):
        SumA += A[r]
        r += 1
    ans += r-l
    if l == r:
        r += 1
    else:
        SumA -= A[l]
print(ans)