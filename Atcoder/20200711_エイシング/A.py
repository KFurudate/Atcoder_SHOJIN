l, r, d = map(int, input().split())

cnt = 0
for _ in range(l, r, d):
    cnt += 1
print(cnt)