x = [0] * 3
y = [0] * 3
z = [0] * 3
for i in range(3):
    x[i], y[i], z[i] = map(int, input().split())

n = int(input())
b = [int(input()) for _ in range(n)]
ans = [x, y, z]

for i in range(3):
    ans.append([x[i], y[i], z[i]])

ans.append([x[0], y[1], z[2]])
ans.append([x[2], y[1], z[0]])

cnt_list = []
for i in range(len(ans)):
    cnt = 0
    for j in list(set(x + y + z) & set(b)):
        if j in ans[i]:
            cnt += 1
    cnt_list.append(cnt)

for cnt in cnt_list:
    if cnt >= 3:
        print('Yes')
        exit()
print('No')