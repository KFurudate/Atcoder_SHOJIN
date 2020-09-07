n, t = map(int, input().split())

A = []
B = []
A_append, B_append = A.append, B.append
for _ in range(n):
    a, b = map(int, input().split())
    A_append(a)
    B_append(b)

sum_B = sum(B)
if sum_B > t:
    print(-1)
    exit()

sum_A = sum(A)
if sum_A <= t:
    print(0)
    exit()

sorted_A = sorted(A)
tmp = t - sum_B
cnt = 0
for a in sorted_A:
    print(tmp, a, cnt)
    tmp -= a
    if tmp < 0:
        print(n-cnt)
        exit()
    cnt += 1
    #print(tmp, a, cnt)


