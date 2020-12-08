n, a, b = map(int, input().split())
SD = [list(map(str, input().split())) for _ in range(n)]

cnt = 0
for s, d in SD:
    d = int(d)
    dis = 0
    if d < a:
        dis = a
    elif a <= d <= b:
        dis = d
    else:
        dis = b

    if s == "East":
        cnt -= dis
    else:
        cnt += dis

if cnt > 0:
    print("West", cnt)
elif cnt < 0:
    print("East", -cnt)
else:
    print(cnt)