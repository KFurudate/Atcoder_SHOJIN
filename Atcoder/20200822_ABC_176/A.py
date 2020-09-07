n, x, t = map(int, input().split())

cnt = 0
while True:
    if x >= n:
        print(cnt)
        break
    cnt += t
    x += x

