# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b

n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]

A = []
B = []
for a, b in AB:
    A.append(a)
    B.append(b)

A = sorted(A)
B = sorted(B)

Entr = A[n//2+1]
Exit = B[n//2+1]
print(Entr, Exit)

cnt = 0
for a, b in AB:
    cnt += abs(Entr-a)
    cnt += abs(Exit-b)
    cnt += abs(Entr-Exit+1)
print(cnt)

