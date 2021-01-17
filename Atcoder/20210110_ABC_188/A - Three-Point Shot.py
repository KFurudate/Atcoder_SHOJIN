x, y = map(int, input().split())

low = min(x, y)
high = max(x, y)
if low + 3 > high:
    print("Yes")
else:
    print("No")