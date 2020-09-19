n = int(input())
D = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for d1, d2 in D:
    if d1 == d2:
        cnt += 1
    elif d1 != d2:
        cnt = 0
    if cnt == 3:
        print("Yes")
        exit()

print("No")
