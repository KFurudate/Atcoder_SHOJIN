n = int(input())
A = list(map(int, input().split()))

cnt, tmp = 0, A[0]
for a in A[1:]:
    if tmp > a:
        cnt += (tmp-a)
    else:
        tmp = a
print(cnt)