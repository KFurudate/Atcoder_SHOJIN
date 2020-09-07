w, h, n = map(int, input().split())
min_X, max_X = 0, w
min_Y, max_Y = 0, h

for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        min_X = max(x, min_X)
    elif a == 2:
        max_X = min(x, max_X)
    elif a == 3:
        min_Y = max(y, min_Y)
    elif a == 4:
        max_Y = min(y, max_Y)

W = max(0, max_X - min_X)
H = max(0, max_Y - min_Y)
print(W*H)

