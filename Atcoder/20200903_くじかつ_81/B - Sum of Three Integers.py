k, s = map(int, input().split())

cnt = 0
for x in range(k):
    for y in range(k):
        for z in range(k):
            if s == x + y + z:
                cnt +=1
print(cnt)