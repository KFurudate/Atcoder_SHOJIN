#x1, y1, r = map(int, input().split())
#x2, y2, x3, y3 = map(int, input().split())

if abs(x1) + r <= abs(y2) \
        and abs(x1) + r <= abs(y3) \
        and abs(y1) + r <= abs(x2) \
        and abs(y1) + r <= abs(x3):
    print("NO")
    print("YES")

elif abs(x1) + r >= abs(y2) \
        and abs(x1) + r >= abs(y3) \
        and abs(y1) + r >= abs(x2) \
        and abs(y1) + r >= abs(x3):
    print("YES")
    print("NO")

else:
    print("YES")
    print("YES")

