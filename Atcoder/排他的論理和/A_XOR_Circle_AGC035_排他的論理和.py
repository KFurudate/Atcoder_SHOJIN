#https://atcoder.jp/contests/agc035/tasks/agc035_a

n = int(input())
A = list(map(int, input().split()))
l, r, SumA, ans = 0, 0, 0, 0

for l in range(n):
    while SumA & A[r] == 0:
        SumA += A[r]
        r += 1
    ans = max(ans, SumA)
    if l == r:
        r += 1
    else:
        SumA -= A[l]
print(ans)
