m, n, N = map(int, input().split())

cnt = 0
cnt += N
tmp2 = 0

while True:
    tmp1 = N // m * n
    tmp2 += N % m
    cnt += tmp1
    N = tmp1

    if N < m and m >= (N + tmp2):
        N += tmp2
        tmp2 = 0
    elif N < m and m < (N + tmp2):
        print(cnt)
        exit()

    print(tmp1, tmp2, N, cnt)

