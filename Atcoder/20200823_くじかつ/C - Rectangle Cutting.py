w, h, x, y = map(int, input().split())

P = 0
if h > w:
    ans = min(x*h, (w-x)*h)

elif h == w:
    if x != 0 and y != 0:
        P = 1
    ans = max(min(x * h, (w - x) * h), min(y * w, (h - y) * w))

else:
    ans = min(y * w, (h - y) * w)

print(ans, P)