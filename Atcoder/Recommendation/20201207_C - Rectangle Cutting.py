W, H, x, y = map(int, input().split())

area = W*H

if (x == W) and (y != H):
    print(min(W * y, (area - W * y)), 0)

elif (x != W) and (y == H):
    print(min(x * H, (area - x * H)), 0)

else:
    area_1 = min(x * H, (area - x * H))
    area_2 = min(W * y, (area - W * y))

    split = 0
    if area_1 == area_2:
        split = 1

    print(max(area_1, area_2), split)

######################
W, H, x, y = map(int, input().split())
S = W * H / 2

if (x == W / 2) and (y == H / 2):
    print(S, 1)
else:
    print(S, 0)
