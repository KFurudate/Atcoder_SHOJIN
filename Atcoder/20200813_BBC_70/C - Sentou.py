n, time = map(int, input().split())
T = list(map(int, input().split()))

cnt = 0
for t in T:
    if t < cnt:
        cnt = t + time
    else:
        cnt += time
    print(t, cnt)

print(cnt)

####################
n, time = map(int, input().split())
T = list(map(int, input().split()))

cnt = time
tmp = T[0]
for t in T[1:]:
    if t <= time + time:
        cnt += t - tmp
    else:
        cnt += time
    tmp = t

print(cnt)