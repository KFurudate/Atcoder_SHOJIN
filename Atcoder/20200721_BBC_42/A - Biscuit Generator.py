a, b, t = map(int, input().split())

cnt = 0
for i in range(1, t+1):
    if i == a:
        cnt += b
print(b)
