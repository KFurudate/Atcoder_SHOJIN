n, x = map(int, input().split())
A = sorted(list(map(int, input().split())))

if sum(A) < x:
    cnt = -1
else:
    cnt = 0

for a in A:
    x -= a
    if x >= 0:
        cnt += 1
    if x <= 0:
        print(cnt)
        exit()
print(cnt)
