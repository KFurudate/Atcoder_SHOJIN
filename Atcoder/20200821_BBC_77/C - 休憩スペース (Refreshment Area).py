n, m, d = map(int, input().split())
dist = [input() for _ in range(n)]
# print(dist)

room = "." * d
cnt = 0
if m >= d:
    for dis in dist:
        for i in range(m - d + 1):
            # print(dis[i:i+d])
            if dis[i:i + d] == room:
                cnt += 1

if n >= d:
    col = [0] * m
    for dis in dist:
        for i in range(m):
            if dis[i] == ".":
                col[i] += 1
                if col[i] >= d:
                    cnt += 1
                #print(cnt, dis[i], col)

            if dis[i] == "#":
                col[i] = 0
print(cnt)