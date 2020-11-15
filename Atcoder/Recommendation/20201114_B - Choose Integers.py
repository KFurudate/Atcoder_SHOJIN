a, b, c = map(int, input().split())


cnt = 0
for _ in range(100001):
    cnt += a
    if (cnt % b) == c:
        print("YES")
        exit()
print("NO")
